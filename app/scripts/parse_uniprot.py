import urllib.request




def parse_uniprot(up_id):
    try:
        with urllib.request.urlopen("http://www.uniprot.org/uniprot/" + up_id + ".txt") as url:
            s = url.read()
        s = s.decode("utf-8")
        s = s.split("\n")
        sequence = ""
        description = ""

        description_found = False
        start = False
        for line in s:
            if line.startswith("//"):
                break
            elif not description_found:
                if line.startswith("DE") and "Full=" in line:
                    description_found = True
                    description = line[line.split("\n")[0].find("Full") + 5:]
            if start:
                sequence += line
            if line.startswith("SQ"):
                start = True
        sequence = sequence.replace(" ", "")
        if len(sequence) > 50:
            return ParsingResult(error=True, error_type="sequence is too long",
                                 description=description, sequence=sequence)
        else:
            return ParsingResult(error=False, error_type="no error",
                                 description=description, sequence=sequence)
    except:
        return ParsingResult(error=True, error_type="Uniprot ID not found", description="", sequence="")
