<?php

/*

Sends z39.50 request to helios.nlib.ee and shows result as json. Inputs (GET parameters) are:
    q - Query string
    r - Row count to return

*/

    $records = (int) urldecode($_GET['r']);
    $query = urldecode($_GET['q']);

    if($records < 1) $records = 1;
    if(!$query) exit('ERROR: No query string');

    header('Content-Type: application/json');
    echo json_encode(getMarc($query, $records));


    //gets MARC21 records from server (as XML) and return those as JSON list
    function getMarc($query, $range) {
        $server = 'helios.nlib.ee:212/innopac';

        $id = yaz_connect($server);
        yaz_syntax($id, "marc21");
        yaz_range($id, 1, $range);
        yaz_search($id, "rpn", "@or @or @attr 1=7 \"$query\" @attr 1=4 \"$query\" @attr 1=1003 \"$query\""); //ISBN or Title or Author - http://www.loc.gov/z3950/agency/defns/bib1.html
        yaz_wait();
        if(yaz_error($id)) exit('ERROR: '. yaz_error($id));

        for ($p = 1; $p <= $range; $p++) {
            $xml = yaz_record($id, $p, "xml");
            if($xml) $result[] = xml2array($xml);
        }

        return $result;
    }


    //convert MARCXML to JSON
    function xml2array($xml_string) {
        $xml = simplexml_load_string($xml_string, 'SimpleXMLElement');

        foreach($xml->leader as $field) {
            $result['000'][]['a'] = strval($field);
        }

        foreach($xml->controlfield as $field) {
            $result[strval($field['tag'])][]['a'] = strval($field);
        }

        foreach($xml->datafield as $field) {
            $data = array();
            foreach($field->subfield as $value) {
                $data[strval($value['code'])] = cleanStr(strval($value));
            }
            $result[strval($field['tag'])][] = $data;
        }

        return $result;
    }


    //trim garbage
    function cleanStr($string) {
        $result = trim($string, ' .:,;/');
        return $result;
    }

?>