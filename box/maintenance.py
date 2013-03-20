import subprocess
from box.config import FarawayBoxConfig

class Maintenance(FarawayBoxConfig):
    daemonDir = "/home/pi/faraway_daemon"
    def status(self):
        if self.attrs["get_update"]:
            self.get_update()
        return self.attrs["reboot"]

    def get_update(self):
        update_cmd = self.update_cmd()
        print "running update command {}".format(" ".join(update_cmd))
        update_process = subprocess.Popen(cmd, cwd=daemonDir)
        if update_process.wait() != 0:
            raise IOError("updating git repo failed")

    def update_cmd(self):
        remote = self.attrs["get_update"][remote]
        branch = self.attrs["get_update"][branch]
        return ["git", "pull", remote, branch]
