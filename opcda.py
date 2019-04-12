from opc import OpenOPC
import time
import writejson

global data
data = []
opc_host = '10.8.8.16'

def start():
    return OpenOPC.client()


def servers(opc):
    return opc.servers(opc_host=opc_host)


# def is_connected():
#     return True

def connect(opc, server):
    try:
        opc.connect(server,opc_host = opc_host)
        info = dict(opc.info())
        if info['OPC Server'] == server:
            connected = True
        else:
            connected = False
    except Exception:
        connected = False
    return connected


def tags(opc):
    paths = []
    f = open('C:/configure.txt', 'r')
    if f == False:
        print "Failed to read the file"
    for line in f:
         paths.append(line.strip('\n'))
    f.close()
    while '' in paths:
        paths.remove('')
    return opc.list(paths = paths,recursive=True)


def read(opc, tags):
    results = opc.read(tags)
    return csv_line(results)


def demux_results(results):
    tags = [tag for tag, value, status, time in results]
    values = [value for tag, value, status, time in results]
    statuses = [status for tag, value, status, time in results]
    times = [time for tag, value, status, time in results]
    return tags, values, statuses, times


def csv_line(results,
             sep=';',
             halt_if_bad=False,
             bad_value='',
             halt_if_not_sync=True,
             include_timestamp=True,
             timestamp_col_name='Timestamp'):
    tags, values, statuses, times = demux_results(results)
    sync = all(times[0] == time for time in times)
    if not sync:
        pass
    all_good = all(status == 'Good' for status in statuses)
    if not all_good:
        pass
    tags_line = sep.join(['Timestamp'] + tags)
    values_line = sep.join([times[0]] + [str(value) for value in values])
    single_data = list(zip(times,tags,values))
    writefile(single_data)
    return tags_line, values_line

def writefile(single_data):
    global last_time
    global data
    if len(data) == 0:
        last_time = time.strftime('%Y-%m-%d-%H-%M',time.localtime())
    data.extend(single_data)
    current_time = time.strftime('%Y-%m-%d-%H-%M',time.localtime())
    if current_time != last_time:
        writejson.writejson(data)
        last_time = current_time
        data = []
