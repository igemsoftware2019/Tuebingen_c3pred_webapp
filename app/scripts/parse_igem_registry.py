import urllib3
import xmltodict
import warnings

from app.scripts.parsing_result import ParsingResult
from Bio import BiopythonWarning
from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC

warnings.simplefilter('ignore', BiopythonWarning)

def get_xml(id):
    url = "http://parts.igem.org/cgi/xml/part.cgi?part=" + id
    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data


def get_part_info(xml):
    part_list = xml["rsbpml"]["part_list"]
    if "ERROR" in part_list.keys():
        return ParsingResult(error=True, error_type="part not found", description=part_list["ERROR"], sequence="")
    else:
        if part_list["part"]["part_type"] == "Coding":
            nt_sequence = part_list["part"]["sequences"]["seq_data"].replace("\n", "")

            # remove start codon
            if nt_sequence.startswith("atg"):
                nt_sequence = Seq(nt_sequence[3:], IUPAC.unambiguous_dna)

            # translate to protein sequence
            prot_sequence = str(translate(nt_sequence))

            # remove characters after stop codon
            prot_sequence = prot_sequence.split("*")[0]

            # discard sequence that are too long for a CPP
            if len(prot_sequence) > 50:
                return ParsingResult(error=True, error_type="sequence is too long",
                                     description=part_list["part"]["part_short_desc"], sequence=prot_sequence)
            else:  # all requirements for prediction passed
                return ParsingResult(error=False, error_type="none", description=part_list["part"]["part_short_desc"],
                                     sequence=prot_sequence)
        else:
            return ParsingResult(error=True, error_type="non-coding sequence",
                                 description=part_list["part"]["part_short_desc"], sequence="")


def get_registry_info(id):
    registry_entry = get_xml(id)
    return get_part_info(registry_entry)
