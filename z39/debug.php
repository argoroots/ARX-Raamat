<?php

    header('Content-Type: text/plain; charset=UTF-8');

    $server = 'helios.nlib.ee:212/innopac';
    $query = utf8_decode($_GET['q']);
    $range = (int) urldecode($_GET['r']);

    if(!$query) $errors[] = 'No query string (GET parameter "q")';
    if(!$range) $errors[] = 'Record count not specified (GET parameter "r")';

    if (!$errors) {
        $id = yaz_connect($server);
        yaz_syntax($id, "usmarc");
        yaz_range($id, 1, $range);
        yaz_search($id, "rpn", "@or @or @attr 1=7 \"$query\" @attr 1=4 \"$query\" @attr 1=1003 \"$query\""); //ISBN or Title or Author - http://www.loc.gov/z3950/agency/defns/bib1.html
        yaz_wait();
        if(yaz_error($id)) $errors[] = yaz_error($id) . ' - ' . yaz_addinfo($id);
    }

    if (!$errors) {
        for ($p = 1; $p <= $range; $p++) {
            echo (yaz_record($id, $p, "string"));
        }
    } else {
        echo "ERROR\n". implode("\n", $errors);
    }

?>