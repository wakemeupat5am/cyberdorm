#==== PREPARATIONS ====

from core.utils import utils
from core.pdfengine import create_pdf_report

import argparse
parser = argparse.ArgumentParser(description="CyberDorm Network Scanner")
parser.add_argument("-t", "--target", required=True, help="Target IP or subnet")
parser.add_argument("-p", "--profile", choices=["fast", "audit", "forensic"], default="fast")
parser.add_argument("-i", "--intensity", type=int, default=3)
parser.add_argument("-v", "--verbose", action="store_true")

#==== MAIN FUNCTION ====

if __name__ == "__main__":
    args = parser.parse_args()
    results = utils(args.target, args.profile, args.intensity)
    create_pdf_report(results)
