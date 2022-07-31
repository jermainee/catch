import subprocess


class AvailabilityChecker:
    def is_available_dns(self, domain):
        return self.__exec("nslookup {} | grep -i \"Can't find\"".format(domain))

    def is_available_whois(self, domain):
        # check .de whois
        return self.__exec("whois {} | grep 'Status: free'".format(domain))

    def __exec(self, command):
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        print(output.returncode)

        return output.returncode == 1
