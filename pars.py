import json
import xml.etree.ElementTree as ET

input_type = input('xml or json?: ')

if input_type == 'xml':
    xml_input = '''<Input>
                    <K>10</K>
                    <Sums>
                        <decimal>1.01</decimal>
                        <decimal>2.02</decimal>
                    </Sums>
                    <Muls>
                        <int>1</int>
                        <int>4</int>
                    </Muls>
                </Input>'''
    print(xml_input)
    root = ET.fromstring(xml_input)
    xml_out = {
        'SumResult': 0,
        'MulResult': 1,
        'SortedInputs': []
    }
    sum = 0
    k = int(root.find('K').text)
    for el in root.find('Sums'):
        sum += float(el.text)
        xml_out['SortedInputs'].append(el.text)

    xml_out['SumResult'] = round(sum * k, 2)

    for el in root.find('Muls'):
        xml_out['MulResult'] *= int(el.text)
        xml_out['SortedInputs'].append(el.text)

    xml_out['SortedInputs'].sort()

    print(xml_out)

elif input_type == 'json':
    jsn = '{"K":10,"Sums":[1.01,2.02],"Muls":[1,4]}'
    jsn_inp = json.loads(jsn)
    jsn_out = {
        'SumResult': 0,
        'MulResult': 1,
        'SortedInputs': []
    }
    k = jsn_inp['K']
    sum = 0
    for el in jsn_inp['Sums']:
        sum += el
        jsn_out['SortedInputs'].append(el)

    jsn_out['SumResult'] = round(sum * k, 2)

    for el in jsn_inp['Muls']:
        jsn_out['MulResult'] *= el
        jsn_out['SortedInputs'].append(el)

    jsn_out['SortedInputs'].sort()
    print(json.dumps(jsn_out))
else:
    print('error')
