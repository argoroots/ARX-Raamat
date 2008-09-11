-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: d1647.mysql.zone.ee
-- Generation Time: Sep 11, 2008 at 09:31 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: 'd1647sd15359'
--

-- --------------------------------------------------------

--
-- Table structure for table 'items'
--

CREATE TABLE items (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  library_id int(11) unsigned NOT NULL default '0',
  media_id int(11) unsigned NOT NULL default '0',
  item_number decimal(14,4) unsigned default NULL,
  barcode varchar(50) collate utf8_estonian_ci default NULL,
  NUMBER_PERIOODIKA varchar(5) collate utf8_estonian_ci NOT NULL,
  KPV_SISSE date default NULL,
  KPV_VALJA date default NULL,
  quantity int(11) unsigned NOT NULL default '1',
  price decimal(14,2) unsigned default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(10) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(10) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY library_id (library_id),
  KEY media_id (media_id),
  KEY item_number (item_number),
  KEY barcode (barcode),
  KEY old_id (old_id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'lendings'
--

CREATE TABLE lendings (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  user_id int(11) unsigned NOT NULL default '0',
  media_id int(11) unsigned NOT NULL default '0',
  item_id int(11) unsigned NOT NULL default '0',
  count int(11) unsigned NOT NULL default '0',
  date_lending datetime default NULL,
  date_due datetime default NULL,
  date_return datetime default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY user_id (user_id),
  KEY media_id (media_id),
  KEY item_id (item_id),
  KEY old_id (old_id)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'libraries'
--

CREATE TABLE libraries (
  id int(11) unsigned NOT NULL auto_increment,
  public tinyint(3) unsigned NOT NULL default '0',
  `name` varchar(50) collate utf8_estonian_ci default NULL,
  web varchar(50) collate utf8_estonian_ci default NULL,
  email varchar(50) collate utf8_estonian_ci default NULL,
  phone varchar(15) collate utf8_estonian_ci default NULL,
  address varchar(50) collate utf8_estonian_ci default NULL,
  city varchar(25) collate utf8_estonian_ci default NULL,
  zip varchar(5) collate utf8_estonian_ci default NULL,
  county varchar(25) collate utf8_estonian_ci default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Table structure for table 'media'
--

CREATE TABLE media (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  mediatype_id int(11) unsigned NOT NULL default '0',
  title varchar(150) collate utf8_estonian_ci default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY mediatype_id (mediatype_id),
  KEY old_id (old_id),
  FULLTEXT KEY title (title)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'mediatypes'
--

CREATE TABLE mediatypes (
  id int(11) unsigned NOT NULL auto_increment,
  `name` varchar(20) collate utf8_estonian_ci default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'media_persons'
--

CREATE TABLE media_persons (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  media_id int(11) unsigned NOT NULL default '0',
  person_id int(11) unsigned NOT NULL default '0',
  tagtype_id int(10) unsigned NOT NULL default '0',
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  deleted_time timestamp NULL default NULL,
  deleted_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY media_id (media_id),
  KEY person_id (person_id),
  KEY persontype_id (tagtype_id),
  KEY old_id (old_id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'persons'
--

CREATE TABLE persons (
  id int(11) unsigned NOT NULL auto_increment,
  firstname varchar(20) collate utf8_estonian_ci NOT NULL,
  lastname varchar(20) collate utf8_estonian_ci NOT NULL,
  birth_date date default NULL,
  teath_date date default NULL,
  nationality varchar(20) collate utf8_estonian_ci default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  UNIQUE KEY `name` (firstname,lastname),
  FULLTEXT KEY firstname (firstname),
  FULLTEXT KEY lastname (lastname)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'sessions'
--

CREATE TABLE sessions (
  id int(11) unsigned NOT NULL auto_increment,
  `time` timestamp NOT NULL default CURRENT_TIMESTAMP,
  sid varchar(200) collate utf8_estonian_ci NOT NULL,
  username varchar(100) collate utf8_estonian_ci NOT NULL,
  ip varchar(15) collate utf8_estonian_ci NOT NULL,
  os varchar(200) collate utf8_estonian_ci NOT NULL,
  PRIMARY KEY  (id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'systemstrings'
--

CREATE TABLE systemstrings (
  id int(11) unsigned NOT NULL auto_increment,
  `name` varchar(50) collate utf8_estonian_ci NOT NULL,
  est varchar(200) collate utf8_estonian_ci default NULL,
  eng varchar(200) collate utf8_estonian_ci default NULL,
  rus varchar(200) collate utf8_estonian_ci default NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'tags'
--

CREATE TABLE tags (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  media_id int(11) unsigned NOT NULL default '0',
  tagtype_id int(11) unsigned NOT NULL default '0',
  `value` varchar(255) collate utf8_estonian_ci default NULL,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  deleted_time timestamp NULL default NULL,
  deleted_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY media_id (media_id),
  KEY old_id (old_id),
  KEY tagtype_id (tagtype_id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'tagtypes'
--

CREATE TABLE tagtypes (
  id int(11) unsigned NOT NULL auto_increment,
  sortorder tinyint(3) unsigned NOT NULL default '0',
  `name` varchar(20) collate utf8_estonian_ci default NULL,
  `type` varchar(4) collate utf8_estonian_ci NOT NULL default 'text',
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'usergroups'
--

CREATE TABLE usergroups (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  `name` varchar(20) collate utf8_estonian_ci default NULL,
  note text collate utf8_estonian_ci,
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY old_id (old_id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'userrights'
--

CREATE TABLE userrights (
  id int(11) unsigned NOT NULL auto_increment,
  public tinyint(11) unsigned NOT NULL default '0',
  `name` varchar(15) collate utf8_estonian_ci default NULL,
  r_admin tinyint(3) unsigned NOT NULL default '0',
  r_library tinyint(3) unsigned NOT NULL default '0',
  r_users tinyint(3) unsigned NOT NULL default '0',
  r_statistics tinyint(3) unsigned NOT NULL default '0',
  r_preferences tinyint(3) unsigned NOT NULL default '0',
  PRIMARY KEY  (id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table 'users'
--

CREATE TABLE users (
  id int(11) unsigned NOT NULL auto_increment,
  old_id varchar(10) collate utf8_estonian_ci default NULL,
  username varchar(100) collate utf8_estonian_ci default NULL,
  `password` varchar(100) collate utf8_estonian_ci default NULL,
  idcard varchar(255) collate utf8_estonian_ci default NULL,
  `language` enum('est','eng','rus') collate utf8_estonian_ci NOT NULL default 'est',
  usergroup_id int(11) unsigned NOT NULL default '0',
  firstname varchar(20) collate utf8_estonian_ci NOT NULL,
  lastname varchar(20) collate utf8_estonian_ci NOT NULL,
  idcode varchar(11) collate utf8_estonian_ci default NULL,
  email varchar(50) collate utf8_estonian_ci default NULL,
  phone varchar(15) collate utf8_estonian_ci default NULL,
  address varchar(50) collate utf8_estonian_ci default NULL,
  city varchar(25) collate utf8_estonian_ci default NULL,
  zip varchar(5) collate utf8_estonian_ci default NULL,
  county varchar(25) collate utf8_estonian_ci default NULL,
  note text collate utf8_estonian_ci,
  login_count int(11) unsigned NOT NULL default '0',
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY old_id (old_id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci PACK_KEYS=0;

-- --------------------------------------------------------

--
-- Table structure for table 'users_libraries'
--

CREATE TABLE users_libraries (
  id int(11) unsigned NOT NULL auto_increment,
  user_id int(11) unsigned NOT NULL default '0',
  library_id int(11) unsigned NOT NULL default '0',
  userright_id int(11) unsigned NOT NULL default '0',
  created_time timestamp NULL default NULL,
  created_user_id int(11) unsigned NOT NULL default '0',
  changed_time timestamp NULL default NULL,
  changed_user_id int(11) unsigned NOT NULL default '0',
  PRIMARY KEY  (id),
  KEY user_id (user_id),
  KEY library_id (library_id),
  KEY userright_id (userright_id)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table '_mahakandmisakt'
--

CREATE TABLE _mahakandmisakt (
  ID int(11) NOT NULL auto_increment,
  VANA_ID int(11) NOT NULL default '0',
  RAAMATUKOGU_FK int(11) NOT NULL default '0',
  MEEDIA_LIIK varchar(2) collate utf8_estonian_ci default NULL,
  NUMBER varchar(25) collate utf8_estonian_ci default NULL,
  POHJUS varchar(50) collate utf8_estonian_ci default NULL,
  KPV datetime default NULL,
  MARKUSED text collate utf8_estonian_ci,
  SYST_MUUDETUD timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  SYST_MUUTJA varchar(50) collate utf8_estonian_ci default NULL,
  PRIMARY KEY  (ID)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;

-- --------------------------------------------------------

--
-- Table structure for table '_saatedokument'
--

CREATE TABLE _saatedokument (
  ID int(11) NOT NULL auto_increment,
  VANA_ID int(11) NOT NULL default '0',
  RAAMATUKOGU_FK int(11) NOT NULL default '0',
  NUMBER varchar(25) collate utf8_estonian_ci default NULL,
  KPV date default NULL,
  VALJAANDJA_FK int(11) NOT NULL default '0',
  MARKUSED text collate utf8_estonian_ci,
  SYST_MUUDETUD timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  SYST_MUUTJA varchar(50) collate utf8_estonian_ci default NULL,
  PRIMARY KEY  (ID)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_estonian_ci;
