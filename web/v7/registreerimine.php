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

	if($_GET['voti']) {
		
		//võtmefaili tegemine
		$row = $Db->Row1('SELECT 
							id, 
							asutus_nimi, 
							asutus_aadress, 
							asutus_linn, 
							asutus_postiindeks, 
							asutus_maakond, 
							asutus_telefon 
							FROM v7_kasutajad 
							WHERE UCASE(TRIM(programm_id)) = UCASE(TRIM(\''.$_GET['id'].'\'))
							ORDER BY reg_kuupaev DESC
							LIMIT 1');
		if($row['id']) {
			$vastus = 'OK: ';
			$vastus .= substr($row['id'].'##################################################', 0, 50);
			$vastus .= substr($row['asutus_nimi'].'##################################################', 0, 50);
			$vastus .= substr($row['asutus_aadress'].'##################################################', 0, 50);
			$vastus .= substr($row['asutus_linn'].'##################################################', 0, 50);
			$vastus .= substr($row['asutus_postiindeks'].'##################################################', 0, 50);
			$vastus .= substr($row['asutus_maakond'].'##################################################', 0, 50);
			$vastus .= substr($row['asutus_telefon'].'##################################################', 0, 50);
			$vastus .= substr('Standard'.'##################################################', 0, 50);
			$Db->Execute('UPDATE v7_kasutajad SET 
							voti_kuupaev = NOW(),
							voti_ip = \''.$kylastajaIP.'\', 
							voti_aadress = \''.$kylastajaADDR.'\'  
							WHERE UCASE(TRIM(programm_id)) = UCASE(TRIM(\''.$_GET['id'].'\'))
							ORDER BY reg_kuupaev DESC
							LIMIT 1');
			
			//emaili sisu koostamine ja saatmine
			$teade .= "ARX-Võti v".$_GET['voti_versioon']."\n";
			$teade .= "\n\n".date('d.m.Y H:i:s')."\n".$kylastajaIP."\n".$kylastajaADDR;
			send_mail("ARX-Raamat v7", "info@arx.ee", "argoroots@gmail.com", "argoroots@gmail.com", "[Key #".$row['id']."] ".$row['asutus_nimi'], $teade);
		} else{
			$vastus = 'VIGA: Programmi ID ei ole õige! Registreerige programm enne võtmefaili genereerimist.';
		}
		//vastuse väljasyamine
		echo $vastus;
		
	} else {
		
		//asutuse nime täitmine
		if(!$_GET['Asutus_Nimi']) {
			if($_GET['Kontaktisik_Nimi']) {
				$_GET['Asutus_Nimi'] = $_GET['Kontaktisik_Nimi'];
			} else {
				$_GET['Asutus_Nimi'] = 'NIMETU';
			}
		}
		
		//eposti loendisse panek
		//$Db->Execute('INSERT INTO arx_postiloend (EMAIL, NUMBER, ARVUTI) VALUES (\''.$senderemail.'\', RAND(),\''.gethostbyaddr($REMOTE_ADDR).' ['.$REMOTE_ADDR.']\')');

		
		//kirje lisamine baasi
		$Db->Execute('INSERT INTO v7_kasutajad SET 
						reg_kuupaev = NOW(),
						reg_ip = \''.$kylastajaIP.'\', 
						reg_aadress = \''.$kylastajaADDR.'\', 
						asutus_nimi = \''.$_GET['Asutus_Nimi'].'\', 
						asutus_reg_nr = \''.$_GET['Asutus_RegNumber'].'\', 
						asutus_rmtk_juhataja = \''.$_GET['Asutus_Juhataja'].'\', 
						asutus_aadress = \''.$_GET['Asutus_Aadress'].'\', 
						asutus_linn = \''.$_GET['Asutus_Linn'].'\', 
						asutus_postiindeks = \''.$_GET['Asutus_Postiindeks'].'\', 
						asutus_maakond = \''.$_GET['Asutus_Maakond'].'\', 
						asutus_telefon = \''.$_GET['Asutus_Telefon'].'\', 
						asutus_email = \''.$_GET['Asutus_Email'].'\', 
						kontaktisik_nimi = \''.$_GET['Kontaktisik_Nimi'].'\', 
						kontaktisik_telefon = \''.$_GET['Kontaktisik_Telefon'].'\', 
						kontaktisik_email = \''.$_GET['Kontaktisik_Email'].'\', 
						programm_versioon = \''.$_GET['Programm_VersiooniNr'].'\', 
						programm_id = \''.$_GET['Programm_ID'].'\'
				');
		$viimaneID = $Db->LastRowId();
		
		//vastuse väljasyamine
		echo "ARX-Raamat REG_OK";
		
		//emaili sisu koostamine ja maili saatmine
		$teade = "Asutus\n";
		$teade .= "  Nimi:     ".$_GET['Asutus_Nimi']."\n";
		$teade .= "  RegNr:    ".$_GET['Asutus_RegNumber']."\n";
		$teade .= "  Juhataja: ".$_GET['Asutus_Juhataja']."\n";
		$teade .= "  Aadress:  ".$_GET['Asutus_Aadress']."\n";
		$teade .= "  Linn:     ".$_GET['Asutus_Linn']."\n";
		$teade .= "  Indeks:   ".$_GET['Asutus_Postiindeks']."\n";
		$teade .= "  Maakond:  ".$_GET['Asutus_Maakond']."\n";
		$teade .= "  Telefon:  ".$_GET['Asutus_Telefon']."\n";
		$teade .= "  Email:    ".$_GET['Asutus_Email']."\n";
		$teade .= "\n";
		$teade .= "Kontaktisik\n";
		$teade .= "  Nimi:     ".$_GET['Kontaktisik_Nimi']."\n";
		$teade .= "  Telefon:  ".$_GET['Kontaktisik_Telefon']."\n";
		$teade .= "  Email:    ".$_GET['Kontaktisik_Email']."\n";
		$teade .= "\n";
		$teade .= "Programm\n";
		$teade .= "  Versioon: ".$_GET['Programm_VersiooniNr']."\n";
		$teade .= "  ID:       ".$_GET['Programm_ID']."\n";
		$teade .= "\n\n".date('d.m.Y H:i:s')."\n".$kylastajaIP."\n".$kylastajaADDR;

		send_mail("ARX-Raamat v7", "info@arx.ee", "argoroots@gmail.com", "argoroots@gmail.com", "[Reg #".$viimaneID."] ".$Asutus_Nimi, $teade);

	}


	function send_mail($fromname, $fromemail, $toname, $toemail, $subject, $message) {
  		$headers .= "MIME-Version: 1.0\r\n";
  		$headers .= "Content-type: text/plain; charset=iso-8859-1\r\n";
  		$headers .= "X-Mailer: PHP ".phpversion()."\r\n";
  		$headers .= "From: ".$fromname." <".$fromemail.">\r\n";
  		return (mail($toname.'<'.$toemail.'>', $subject, $message, $headers));
	}
?>