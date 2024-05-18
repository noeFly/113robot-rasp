from xml.etree.ElementTree import parse


def parse_xml(file_path: str, data_id: str) -> list:
    tree = parse(file_path)
    root = tree.getroot()

    if data_id == 'O-A0002-002':
        rains: list = []
        for station in root.findall('.//{urn:cwa:gov:tw:cwacommon:0.1}Station'):
            station_name = station.find('{urn:cwa:gov:tw:cwacommon:0.1}StationId').text  # type: ignore
            if station_name == "A1A9W0":  # 陽明高中
                for precipitation_elem in station.iter('{urn:cwa:gov:tw:cwacommon:0.1}Precipitation'):
                    rains.append(precipitation_elem.text)
        return rains
