<?php

// TbsSql Engine
// Version 1.01, 2006-12-28, Skrol29
class clsTbsSql {

	function clsTbsSql($srv='',$uid='',$pwd='',$db='',$drv='') {
		// Default values (defined here to be compatible with both PHP 4 & 5)
		$this->Id = false;
		$this->Mode = 1; // 0=silent, 1=normal, 2=debug, 3=trace
		// Try to connect when instance is created
		if ($srv!=='') $this->Connect($srv,$uid,$pwd,$db,$drv);
		$this->_Dbs_Prepare();
		// Hook for the TinyButStrong Template Engine
		$GLOBALS['_TBS_UserFctLst']['k:tbssql'] = array('type'=>4,'open'=>array(&$this,'_Dbs_RsOpen'),'fetch'=>array(&$this,'_Dbs_RsFetch'),'close'=>array(&$this,'_Dbs_RsClose'));
	}

// Public methods
	
	function Connect($srv,$uid,$pwd,$db,$drv='') {
		$this->Id = $this->_Dbs_Connect($srv,$uid,$pwd,$db,$drv);
  	if ($this->Id===false) return $this->_SqlError(false);
		return true;
	}

	function Close() {
		if ($this->Id!==false) $this->_Dbs_Close();
	}

	function Execute($Sql) {

		$ArgLst = func_get_args();
		$this->_SqlProtect($Sql,$ArgLst,1);
		$RsId = $this->_Dbs_RsOpen(null,$Sql);
		if ($RsId===false) return $this->_SqlError($this->Id);

		$this->_Dbs_RsClose($RsId);
		return true;

	}

	function Value($DefVal,$Sql) {

		$ArgLst = func_get_args();
		$this->_SqlProtect($Sql,$ArgLst,2);
		$RsId = $this->_Dbs_RsOpen(null,$Sql);
		if ($RsId===false) return $this->_SqlError($this->Id);

		$Row = $this->_Dbs_RsFetch($RsId);
		if ($Row===false) {
			$x = $DefVal;
		} else {
			$x = reset($Row);
		}

		$this->_Dbs_RsClose($RsId);
		return $x;

	}

	function Row1($Sql) {

		$ArgLst = func_get_args();
		$this->_SqlProtect($Sql,$ArgLst,1);
		$RsId = $this->_Dbs_RsOpen(null,$Sql);
		if ($RsId===false) return $this->_SqlError($this->Id);

		$x = $this->_Dbs_RsFetch($RsId);

		$this->_Dbs_RsClose($RsId);
		return $x;

	}

	function Rows($Sql) {
		
		$ArgLst = func_get_args();
		$this->_SqlProtect($Sql,$ArgLst,1);
		$RsId = $this->_Dbs_RsOpen(null,$Sql);
		if ($RsId===false) return $this->_SqlError($this->Id);

		$x = array();
		while ($r = $this->_Dbs_RsFetch($RsId)) {
			$x[] = $r;
		}

		$this->_Dbs_RsClose($RsId);
		return $x;

	}

	function AffectedRows() {
		return $this->_Dbs_AffectedRows();
	}

	function LastRowId() {
		return $this->_Dbs_LastRowId();
	}

// Private methods

	function _SqlError($ObjId) {
		if ($this->Mode==0) return;
		$x =  'Database error message: '.$this->_Dbs_Error($ObjId);
		if ($this->Mode==2) $x .= "\r\nSQL = ".$this->LastSql;
		$this->_SqlMsg($x);
		return false;
	}

	function _SqlMsg($Txt,$Color='#FF0000') {
		if ($this->Mode!=0) {
			echo '<div style="color: '.$Color.';">[TbsSql] '.nl2br(htmlentities($Txt)).'</div>'."\r\n";
			flush();
		}
	}
	
	function _SqlDate($Date,$Mode) {
		// Return the date formated for the current Database
		if (is_string($Date)) {
			$x = strtotime($Date);
			if (($x===-1) or ($x===false)) {
				// display error message
				$this->_SqlMsg('Date value not recognized: '.$Date);
				$Mode = 0; // Try with the string mode
				$x = $Date;
			}
		} else {
			$x = $Date;
		}
		return $this->_Dbs_Date($x,$Mode);
	}
	
	function _SqlProtect(&$Sql,&$ArgLst,$IdxStart) {
	// Replace all %i% and @i@ figures by corresponding protected values
		$IdxMax = count($ArgLst) - 1;
		for ($i=$IdxStart;$i<=$IdxMax;$i++) {
			// Simple value
			$n = $i - $IdxStart + 1;
			$tag = '%'.$n.'%';
			if (strpos($Sql,$tag)!==false) {
				$x = $this->_Dbs_ProtectStr(''.$ArgLst[$i]);
				$Sql = str_replace($tag,$x,$Sql) ;
			}
			// String value
			$tag = '@'.$n.'@';
			if (strpos($Sql,$tag)!==false) {
				$x = '\''.$this->_Dbs_ProtectStr(''.$ArgLst[$i]).'\'';
				$Sql = str_replace($tag,$x,$Sql) ;
			}
			// Date value
			$tag = '#'.$n.'#';
			if (strpos($Sql,$tag)!==false) {
				$x = $this->_SqlDate($ArgLst[$i],1);
				$Sql = str_replace($tag,$x,$Sql) ;
			}
			// Date and time value
			$tag = '~'.$n.'~';
			if (strpos($Sql,$tag)!==false) {
				$x = $this->_SqlDate($ArgLst[$i],2);
				$Sql = str_replace($tag,$x,$Sql) ;
			}
		}
		if ($this->Mode==2) {
			$this->LastSql = $Sql;
		} elseif ($this->Mode==3) {
			$this->_SqlMsg('Trace SQL: '.$Sql,'#663399');
		}
	}

// -------------------------------
// Specific to the Database System
// -------------------------------

// Database Engine: MySQL 
// Version 1.02, 2006-10-12, Skrol29
	
	function _Dbs_Prepare() {
		if (@mysql_ping()) { // Check if a MySQL connection already exist
			$this->Id = true;
		}
	}

	function _Dbs_Connect($srv,$uid,$pwd,$db,$drv) {
		$Id = @mysql_connect($srv,$uid,$pwd);
		if (($Id!==false) and ($db!=='')) {
			if (!@mysql_select_db($db)) $this->_SqlError(false);
		}
		return $Id;
	}

	function _Dbs_Close() {
		if (is_resource($this->Id)) {
			return @mysql_close($this->Id);
		} else {
			return @mysql_close();
		}
	}

	function _Dbs_Error($ObjId) {
		if (is_resource($this->Id)) {
			return @mysql_error($ObjId);
		} else {
			return @mysql_error();
		}
	}
	
	function _Dbs_RsOpen($Src,$Sql) {
	// $Src is only for compatibility with TinyButStrong
		if (is_resource($this->Id)) {
			return @mysql_query($Sql,$this->Id);
		} else {
			return @mysql_query($Sql);
		}
	}

	function _Dbs_RsFetch(&$RsId) {
		return mysql_fetch_assoc($RsId);
	}

	function _Dbs_RsClose(&$RsId) {
		if ($RsId===true)  return true;
		return @mysql_free_result($RsId);
	}
	
	function _Dbs_ProtectStr($Txt) {
		return mysql_escape_string($Txt);
	}
	
	function _Dbs_Date($Timestamp,$Mode) {
		switch ($Mode) {
		case 1:
			// Date only
			return '\''.date('Y-m-d',$Timestamp).'\'';
		case 2:
			// Date and time
			return '\''.date('Y-m-d H:i:s',$Timestamp).'\'';
		case 0:
			// Value is a string
			return '\''.$this->_Dbs_ProtectStr($Timestamp).'\'';
		default:
			// Error in date recognization
			return '\'0000-00-00\'';
		}  
	}

	function _Dbs_LastRowId() {
		return $this->Value(false,'SELECT LAST_INSERT_ID()');
	}
	
	function _Dbs_AffectedRows() {
		if (is_resource($this->Id)) {
			return mysql_affected_rows($this->Id);
		} else {
			return mysql_affected_rows();
		}
		
	}

}



?>
