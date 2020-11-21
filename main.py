import speedtest
import platform,socket,re,uuid,json,psutil,logging, subprocess, glob


def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    # results = speedtest.shell()
    # print(results.dict())
    # system_info = json.loads(getSystemInfo())
    # print(system_info)
    release_info = subprocess.run(['cat', '--'] + glob.glob('/etc/*-release'), stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(release_info.split('\n'))