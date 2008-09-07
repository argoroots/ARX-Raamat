<?php

	include_once('tbssql_mysql.php');

	$server = 'd1647.mysql.zone.ee';
	$andmebaas = 'd1647sd15358';
	$kasutajanimi = 'd1647sa23793';
	$parool = 'Arx123';
	$kylastajaIP = $_SERVER['REMOTE_ADDR'];
	$kylastajaADDR = gethostbyaddr($_SERVER['REMOTE_ADDR']);

	// avab andmebaasi
	$Db = new clsTbsSQL($server, $kasutajanimi, $parool, $andmebaas);
	$Db->Mode = 1;

	if($Db->Value(0, 'SELECT id FROM v7_kasutajad WHERE id = %1% AND UCASE(TRIM(programm_id)) = UCASE(TRIM(@2@))', $_GET['Asutus_ID'], $_GET['Programm_ID'])==0) {
		//raamatukogu andmeid pole v7_kasutajad tabelis, otsime tabelist v7_vana
		
		$teade = print_r($_GET, true);
		$teade .= "\n\n".date('d.m.Y H:i:s')."\n".$kylastajaIP."\n".$kylastajaADDR;
		//send_mail("ARX-Raamat v7", "info@arx.ee", "argoroots@gmail.com", "argoroots@gmail.com", "[Vana] ". $_GET['Asutus_Nimi'], $teade);
		
		$Db->Execute('INSERT INTO v7_kasutajad (
						id,
						reg_kuupaev,
						asutus_nimi, 
						asutus_aadress, 
						asutus_linn, 
						asutus_postiindeks, 
						asutus_maakond, 
						asutus_telefon, 
						asutus_email, 
						kontaktisik_nimi, 
						kontaktisik_telefon, 
						kontaktisik_email, 
						programm_versioon, 
						programm_id,
						viimati_kuupaev, 
						viimati_ip, 
						viimati_aadress, 
						viimati_kord 
					) SELECT
						id,
						leping_kuupaev,
						asutus_nimi, 
						asutus_aadress, 
						asutus_linn, 
						asutus_postiindeks, 
						asutus_maakond, 
						asutus_telefon, 
						asutus_email, 
						kontaktisik_nimi, 
						kontaktisik_telefon, 
						kontaktisik_email, 
						@1@, 
						@2@,
						NOW(), 
						@3@, 
						@4@, 
						1 
					FROM v7_ostjad
					WHERE id = %5%
				', $_GET['Programm_Versioon'], $_GET['Programm_ID'], $kylastajaIP, $kylastajaADDR, $_GET['Asutus_ID']);
	} else {
		//raamatukogu on v7_kasutajad tabelis ja uuendatakse viimati_ infot
		$Db->Execute('UPDATE v7_kasutajad SET 
						viimati_kuupaev = NOW(), 
						viimati_ip = @1@, 
						viimati_aadress = @2@, 
						viimati_kord = (viimati_kord + 1) 
						WHERE id = %3% 
						AND UCASE(TRIM(programm_id)) = UCASE(TRIM(@4@))
				', $kylastajaIP, $kylastajaADDR, $_GET['Asutus_ID'], $_GET['Programm_ID']);
	}
	
	$Db->Execute('UPDATE v7_ostjad SET todo = \'V7_KASUTAJAD\' WHERE id = %1%', $_GET['Asutus_ID']);
	
	echo 'ARX-Raamat 7.0.150';
	
	function send_mail($fromname, $fromemail, $toname, $toemail, $subject, $message) {
  		$headers .= "MIME-Version: 1.0\r\n";
  		$headers .= "Content-type: text/plain; charset=iso-8859-1\r\n";
  		$headers .= "X-Mailer: PHP ".phpversion()."\r\n";
  		$headers .= "From: ".$fromname." <".$fromemail.">\r\n";
  		return (mail($toname.'<'.$toemail.'>', $subject, $message, $headers));
	}

?>