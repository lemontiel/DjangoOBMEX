-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.2.6-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para datosobmex
CREATE DATABASE IF NOT EXISTS `datosobmex` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `datosobmex`;

-- Volcando estructura para tabla datosobmex.aplicacionobmex_comentario
CREATE TABLE IF NOT EXISTS `aplicacionobmex_comentario` (
  `id_Comentario` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `texto` longtext NOT NULL,
  PRIMARY KEY (`id_Comentario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_contacto
CREATE TABLE IF NOT EXISTS `aplicacionobmex_contacto` (
  `id_Contacto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(90) NOT NULL,
  `apellidoM` varchar(45) NOT NULL,
  `apellidoP` varchar(45) NOT NULL,
  `cargo` varchar(30) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `telefono_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Contacto`),
  KEY `aplicacionobmex_contacto_telefono_id_685cc599_fk` (`telefono_id`),
  CONSTRAINT `aplicacionobmex_contacto_telefono_id_685cc599_fk` FOREIGN KEY (`telefono_id`) REFERENCES `aplicacionobmex_telefono` (`id_Telefono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_contacto_comentarios
CREATE TABLE IF NOT EXISTS `aplicacionobmex_contacto_comentarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contacto_id` int(11) NOT NULL,
  `comentario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aplicacionobmex_contacto_contacto_id_comentario_i_3701ea5f_uniq` (`contacto_id`,`comentario_id`),
  KEY `aplicacionobmex_cont_comentario_id_c3397f28_fk_aplicacio` (`comentario_id`),
  CONSTRAINT `aplicacionobmex_cont_comentario_id_c3397f28_fk_aplicacio` FOREIGN KEY (`comentario_id`) REFERENCES `aplicacionobmex_comentario` (`id_Comentario`),
  CONSTRAINT `aplicacionobmex_cont_contacto_id_fd32cdb5_fk_aplicacio` FOREIGN KEY (`contacto_id`) REFERENCES `aplicacionobmex_contacto` (`id_Contacto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_contacto_cursos
CREATE TABLE IF NOT EXISTS `aplicacionobmex_contacto_cursos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contacto_id` int(11) NOT NULL,
  `curso_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aplicacionobmex_contacto_contacto_id_curso_id_5478ff8a_uniq` (`contacto_id`,`curso_id`),
  KEY `aplicacionobmex_cont_curso_id_899297db_fk_aplicacio` (`curso_id`),
  CONSTRAINT `aplicacionobmex_cont_contacto_id_40b583db_fk_aplicacio` FOREIGN KEY (`contacto_id`) REFERENCES `aplicacionobmex_contacto` (`id_Contacto`),
  CONSTRAINT `aplicacionobmex_cont_curso_id_899297db_fk_aplicacio` FOREIGN KEY (`curso_id`) REFERENCES `aplicacionobmex_curso` (`id_Curso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_contacto_pedido
CREATE TABLE IF NOT EXISTS `aplicacionobmex_contacto_pedido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contacto_id` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aplicacionobmex_contacto_contacto_id_pedido_id_d85c53aa_uniq` (`contacto_id`,`pedido_id`),
  KEY `aplicacionobmex_cont_pedido_id_434c8125_fk_aplicacio` (`pedido_id`),
  CONSTRAINT `aplicacionobmex_cont_contacto_id_c91fe31a_fk_aplicacio` FOREIGN KEY (`contacto_id`) REFERENCES `aplicacionobmex_contacto` (`id_Contacto`),
  CONSTRAINT `aplicacionobmex_cont_pedido_id_434c8125_fk_aplicacio` FOREIGN KEY (`pedido_id`) REFERENCES `aplicacionobmex_pedido` (`id_Pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_curso
CREATE TABLE IF NOT EXISTS `aplicacionobmex_curso` (
  `id_Curso` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `hora` time(6) NOT NULL,
  `costo` double NOT NULL,
  `instructor` varchar(130) NOT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Curso`),
  KEY `aplicacionobmex_curs_direccion_id_240c5b70_fk_aplicacio` (`direccion_id`),
  CONSTRAINT `aplicacionobmex_curs_direccion_id_240c5b70_fk_aplicacio` FOREIGN KEY (`direccion_id`) REFERENCES `aplicacionobmex_direccion` (`id_Direccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_curso_participantes
CREATE TABLE IF NOT EXISTS `aplicacionobmex_curso_participantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `curso_id` int(11) NOT NULL,
  `contacto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aplicacionobmex_curso_pa_curso_id_contacto_id_f17502e7_uniq` (`curso_id`,`contacto_id`),
  KEY `aplicacionobmex_curs_contacto_id_132cbef5_fk_aplicacio` (`contacto_id`),
  CONSTRAINT `aplicacionobmex_curs_contacto_id_132cbef5_fk_aplicacio` FOREIGN KEY (`contacto_id`) REFERENCES `aplicacionobmex_contacto` (`id_Contacto`),
  CONSTRAINT `aplicacionobmex_curs_curso_id_1ba08150_fk_aplicacio` FOREIGN KEY (`curso_id`) REFERENCES `aplicacionobmex_curso` (`id_Curso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_direccion
CREATE TABLE IF NOT EXISTS `aplicacionobmex_direccion` (
  `id_Direccion` int(11) NOT NULL AUTO_INCREMENT,
  `calle` varchar(50) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `colonia` varchar(25) NOT NULL,
  `entidad` varchar(30) NOT NULL,
  `delegacion` varchar(30) NOT NULL,
  `pais` varchar(30) NOT NULL,
  `numero_2` varchar(30) NOT NULL,
  `entreCalle_1` varchar(30) NOT NULL,
  `entreCalle_2` varchar(30) NOT NULL,
  `estado` varchar(2) NOT NULL,
  PRIMARY KEY (`id_Direccion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_institucion
CREATE TABLE IF NOT EXISTS `aplicacionobmex_institucion` (
  `id_Institucion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `rfc` varchar(16) DEFAULT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  `telefono_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Institucion`),
  KEY `aplicacionobmex_inst_direccion_id_c201d196_fk_aplicacio` (`direccion_id`),
  KEY `aplicacionobmex_institucion_telefono_id_6a679280_fk` (`telefono_id`),
  CONSTRAINT `aplicacionobmex_inst_direccion_id_c201d196_fk_aplicacio` FOREIGN KEY (`direccion_id`) REFERENCES `aplicacionobmex_direccion` (`id_Direccion`),
  CONSTRAINT `aplicacionobmex_institucion_telefono_id_6a679280_fk` FOREIGN KEY (`telefono_id`) REFERENCES `aplicacionobmex_telefono` (`id_Telefono`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_institucion_contacto
CREATE TABLE IF NOT EXISTS `aplicacionobmex_institucion_contacto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `institucion_id` int(11) NOT NULL,
  `contacto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aplicacionobmex_instituc_institucion_id_contacto__71b794a7_uniq` (`institucion_id`,`contacto_id`),
  KEY `aplicacionobmex_inst_contacto_id_8407447c_fk_aplicacio` (`contacto_id`),
  CONSTRAINT `aplicacionobmex_inst_contacto_id_8407447c_fk_aplicacio` FOREIGN KEY (`contacto_id`) REFERENCES `aplicacionobmex_contacto` (`id_Contacto`),
  CONSTRAINT `aplicacionobmex_inst_institucion_id_7fd36bcb_fk_aplicacio` FOREIGN KEY (`institucion_id`) REFERENCES `aplicacionobmex_institucion` (`id_Institucion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_institucion_pedido
CREATE TABLE IF NOT EXISTS `aplicacionobmex_institucion_pedido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `institucion_id` int(11) NOT NULL,
  `pedido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `aplicacionobmex_instituc_institucion_id_pedido_id_9c3c8b9d_uniq` (`institucion_id`,`pedido_id`),
  KEY `aplicacionobmex_inst_pedido_id_f2ca0fa2_fk_aplicacio` (`pedido_id`),
  CONSTRAINT `aplicacionobmex_inst_institucion_id_84006728_fk_aplicacio` FOREIGN KEY (`institucion_id`) REFERENCES `aplicacionobmex_institucion` (`id_Institucion`),
  CONSTRAINT `aplicacionobmex_inst_pedido_id_f2ca0fa2_fk_aplicacio` FOREIGN KEY (`pedido_id`) REFERENCES `aplicacionobmex_pedido` (`id_Pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_inventario
CREATE TABLE IF NOT EXISTS `aplicacionobmex_inventario` (
  `id_Producto` int(11) NOT NULL AUTO_INCREMENT,
  `generacion` int(11) NOT NULL,
  `existencias` int(11) NOT NULL,
  `maxStock` int(11) NOT NULL,
  PRIMARY KEY (`id_Producto`),
  UNIQUE KEY `aplicacionobmex_inventario_generacion_0782c46e_uniq` (`generacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_pedido
CREATE TABLE IF NOT EXISTS `aplicacionobmex_pedido` (
  `id_Pedido` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `monto` double NOT NULL,
  `tipoSilla_id` int(11) NOT NULL,
  `hora` time(6) NOT NULL,
  `cantidad` int(11) NOT NULL,
  PRIMARY KEY (`id_Pedido`),
  KEY `aplicacionobmex_pedido_tipoSilla_id_54ef6026_fk` (`tipoSilla_id`),
  CONSTRAINT `aplicacionobmex_pedido_tipoSilla_id_54ef6026_fk` FOREIGN KEY (`tipoSilla_id`) REFERENCES `aplicacionobmex_inventario` (`id_Producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.aplicacionobmex_telefono
CREATE TABLE IF NOT EXISTS `aplicacionobmex_telefono` (
  `id_Telefono` int(11) NOT NULL AUTO_INCREMENT,
  `lada` int(11) DEFAULT NULL,
  `numero` int(11) NOT NULL,
  `extencion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Telefono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
-- Volcando estructura para tabla datosobmex.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- La exportación de datos fue deseleccionada.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
