import dotbot
import subprocess


def _apm_get_installed_packages():
    cmd = ['apm', 'list', '-i', '-p', '-b']
    raw = subprocess.check_output(cmd).decode()
    packages = []
    for line in raw.strip().splitlines():
        package, _ = line.split('@')
        packages.append(package)
    return packages


def _apm_install_package(package):
    cmd = ['apm', 'install', package]
    with open('/dev/null', 'w') as devnull:
        returncode = subprocess.call(cmd, stdout=devnull, stderr=devnull)
    return returncode == 0


class Atom(dotbot.Plugin):
    def __init__(self, *args, **kwargs):
        super(Atom, self).__init__(*args, **kwargs)
        self._packages = None

    def can_handle(self, directive):
        return directive == 'atom'

    def handle(self, directive, data):
        try:
            if directive == 'atom':
                success = True
                self._bootstrap()
                for package in data:
                    if not self._install_package(package):
                        success = False
                if success:
                    self._log.info('All atom packages have been installed')
                else:
                    self._log.error('Some atom packages were not'
                                    'installed correctly')
                return success
            return False
        except Exception as e:
            self._log.error('Error: %s' % e)
            return False

    def _install_package(self, package):
        if package in self._packages:
            self._log.lowinfo("Atom package already installed: %s" % package)
            return True
        if not _apm_install_package(package):
            self._log.warning("Failed to install Atom package: %s" % package)
            return False
        self._log.lowinfo("Installed Atom package: %s" % package)
        return True

    def _bootstrap(self):
        if self._packages is None:
            self._check_apm()
            self._packages = _apm_get_installed_packages()

    def _check_apm(self):
        try:
            with open('/dev/null', 'w') as devnull:
                subprocess.check_call(['apm', '-v'], stdout=devnull,
                                      stderr=devnull)
        except Exception:
            self._log.error("Atom package manager not usable: "
                            "Failed to run 'apm' command")
            raise RuntimeError('Failed to run atom package manger (apm)')
