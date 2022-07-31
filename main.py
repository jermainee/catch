from src.AvailabilityChecker import AvailabilityChecker

checker = AvailabilityChecker()

domain = "casalist.de"

if not checker.is_available_dns(domain):
    print("Available dns")
else:
    print("Not available dns")

if not checker.is_available_whois(domain):
    print("Available whois")
else:
    print("Not available whois")
