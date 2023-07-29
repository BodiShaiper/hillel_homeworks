from HW13.csv_adapter import CSVAdapter


class XMLFormatter:
    def format_data(self, data):
        xml = ''
        for item in data:
            xml += '<record>\n'
            for key, value in item.items():
                xml += f"    <{key}>{value}</{key}>\n"
            xml += '</record>\n'

        return xml


def main():
    filename = 'data.txt'  # Replace with the actual filename

    adapter = CSVAdapter(filename)
    data = adapter.convert_from_txt_to_html()

    formatter = XMLFormatter()
    xml_output = formatter.format_data(data)

    print(xml_output)


if __name__ == '__main__':
    main()
