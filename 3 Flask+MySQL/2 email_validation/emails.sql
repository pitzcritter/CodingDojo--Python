CREATE DATABASE  IF NOT EXISTS `emails` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `emails`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: emails
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `emails`
--

DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emails` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updatd_at` datetime NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emails`
--

LOCK TABLES `emails` WRITE;
/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
INSERT INTO `emails` VALUES (1,'me@there','2018-01-09 10:42:41','2018-01-09 10:42:41'),(2,'this@whatever.com','2018-01-09 11:52:09','2018-01-09 11:52:09'),(3,'this@whatever.com','2018-01-09 11:52:57','2018-01-09 11:52:57'),(4,'otherthis@whatever.com','2018-01-09 12:27:43','2018-01-09 12:27:43'),(5,'other@whatever.com','2018-01-09 12:29:32','2018-01-09 12:29:32'),(6,'others@whatever.com','2018-01-09 12:30:03','2018-01-09 12:30:03'),(7,'othersy@whatever.com','2018-01-09 12:31:44','2018-01-09 12:31:44'),(8,'lizardlarry@podunk.com','2018-01-09 12:39:38','2018-01-09 12:39:38'),(9,'lizard@podunk.com','2018-01-09 12:40:41','2018-01-09 12:40:41'),(10,'lizarsdly@podunk.com','2018-01-09 12:46:35','2018-01-09 12:46:35'),(11,'lizary@podunk.com','2018-01-09 12:48:16','2018-01-09 12:48:16'),(12,'lizarsy@podunk.com','2018-01-09 12:49:58','2018-01-09 12:49:58'),(13,'lizarsz@podunk.com','2018-01-09 12:53:37','2018-01-09 12:53:37'),(14,'lizrsz@podunk.com','2018-01-09 12:59:18','2018-01-09 12:59:18'),(15,'liz@podunk.com','2018-01-09 13:08:21','2018-01-09 13:08:21'),(16,'lizzy@podunk.com','2018-01-09 13:10:49','2018-01-09 13:10:49'),(17,'lizzily@podunk.com','2018-01-09 13:12:02','2018-01-09 13:12:02'),(18,'crapilup@y.com','2018-01-09 13:14:41','2018-01-09 13:14:41'),(19,'grum@y.com','2018-01-09 13:32:34','2018-01-09 13:32:34'),(20,'grump@y.com','2018-01-09 13:34:46','2018-01-09 13:34:46'),(21,'grumpy@y.com','2018-01-09 13:35:21','2018-01-09 13:35:21'),(22,'grumppy@y.com','2018-01-09 13:35:40','2018-01-09 13:35:40'),(23,'grxumppy@y.com','2018-01-09 13:36:21','2018-01-09 13:36:21'),(24,'grxumdppy@y.com','2018-01-09 13:36:38','2018-01-09 13:36:38'),(25,'grxumdpspy@y.com','2018-01-09 13:38:06','2018-01-09 13:38:06'),(26,'grxusmdpspy@y.com','2018-01-09 13:39:16','2018-01-09 13:39:16'),(27,'grxusszmdpspy@y.com','2018-01-09 13:40:38','2018-01-09 13:40:38'),(28,'grxuzmdpspy@y.com','2018-01-09 13:42:27','2018-01-09 13:42:27'),(29,'ay@y.com','2018-01-09 13:45:39','2018-01-09 13:45:39'),(30,'ab@y.com','2018-01-09 13:45:56','2018-01-09 13:45:56'),(31,'abc@y.com','2018-01-09 13:46:54','2018-01-09 13:46:54'),(32,'abcd@y.com','2018-01-09 13:48:57','2018-01-09 13:48:57'),(33,'abcde@y.com','2018-01-09 13:52:48','2018-01-09 13:52:48'),(34,'abcdef@y.com','2018-01-09 13:53:11','2018-01-09 13:53:11'),(35,'abcdeff@y.com','2018-01-09 13:54:23','2018-01-09 13:54:23'),(36,'abcdefg@y.com','2018-01-09 13:55:50','2018-01-09 13:55:50'),(37,'abcdefgh@y.com','2018-01-09 13:58:07','2018-01-09 13:58:07'),(38,'abcdefghi@y.com','2018-01-09 13:59:45','2018-01-09 13:59:45'),(39,'abcdefghij@y.com','2018-01-09 14:00:53','2018-01-09 14:00:53'),(40,'abcdefghijk@y.com','2018-01-09 14:02:59','2018-01-09 14:02:59'),(41,'abcdefghijkl@y.com','2018-01-09 14:03:43','2018-01-09 14:03:43');
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-09 14:22:42
