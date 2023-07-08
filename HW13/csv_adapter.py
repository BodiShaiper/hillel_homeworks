class CSVAdapter:
    def __init__(self, filename):
        self.filename = filename

    def convert_from_txt_to_html(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

            if len(lines) < 2:
                raise ValueError("File does not contain enough data.")

            headers = lines[0].strip().split(',')
            data = []
            for line in lines[1:]:
                values = line.strip().split(',')
                if len(headers) != len(values):
                    raise ValueError("Mismatch in number of headers and data columns.")
                data.append(dict(zip(headers, values)))

            return data
