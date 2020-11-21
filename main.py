import speedtest
import platform, socket, re, uuid, json, logging, subprocess, glob


def getSystemInfo():
    try:
        info = {}
        info["platform"] = platform.system()
        info["platform-release"] = platform.release()
        info["platform-version"] = platform.version()
        info["architecture"] = platform.machine()
        # info
        # ["hostname"] = socket.gethostname()
        # info["ip-address"] = socket.gethostbyname(socket.gethostname())
        # info["mac-address"] = ":".join(re.findall("..", "%012x" % uuid.getnode()))
        info["processor"] = platform.processor()
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def get_release_info():
    release_info = subprocess.run(
        ["cat", "--"] + glob.glob("/etc/*-release"), stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    release_info = release_info.split("\n")
    # print(release_info)
    output = {"extras": []}
    for entry in release_info:
        try:
            key_val = entry.split("=")
            output[key_val[0]] = key_val[1].replace('"', "")
        except:
            output["extras"].append(entry)
    return output


if __name__ == "__main__":
    # results = speedtest.shell()
    # print(results.dict())
    system_info = json.loads(getSystemInfo())
    # print(system_info)
    release_info = get_release_info()
    output = {
        "system_info": system_info,
        # "speedtest_info": results.dict(),
        "Linux_info": release_info,
    }
    print(json.dumps(output))
