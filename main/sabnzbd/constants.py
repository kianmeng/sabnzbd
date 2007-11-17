#!/usr/bin/python -OO
# Copyright 2005 Gregor Kaufmann <tdian@users.sourceforge.net>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

PNFO_REPAIR_FIELD = 0
PNFO_UNPACK_FIELD = 1
PNFO_DELETE_FIELD = 2
PNFO_SCRIPT_FIELD = 3
PNFO_NZO_ID_FIELD = 4
PNFO_FILENAME_FIELD = 5
PNFO_UNPACKSTRHT_FIELD = 6
PNFO_BYTES_LEFT_FIELD = 7
PNFO_BYTES_FIELD = 8
PNFO_AVG_DATE_FIELD = 9
PNFO_FINISHED_FILES_FIELD = 10
PNFO_ACTIVE_FILES_FIELD = 11
PNFO_QUEUED_FILES_FIELD = 12

QNFO_BYTES_FIELD = 0
QNFO_BYTES_LEFT_FIELD = 1
QNFO_PNFO_LIST_FIELD = 2

ANFO_ARTICLE_SUM_FIELD = 0
ANFO_CACHE_SIZE_FIELD = 1
ANFO_CACHE_LIMIT_FIELD = 2

GIGI = float(2 ** 30)
MEBI = float(2 ** 20)
KIBI = float(2 ** 10)

MY_NAME = 'SABnzbd'

STAGENAMES = {1:"Par2", 2:"Unrar", 3:"Unzip", 4:"Filejoin"}

BYTES_FILE_NAME  = 'bytes.sab'
QUEUE_FILE_NAME  = 'queue.sab'
RSS_FILE_NAME    = 'rss.sab'

DEF_DOWNLOAD_DIR = 'incomplete'
DEF_COMPLETE_DIR = 'usenet'
DEF_CACHE_DIR    = 'cache'
DEF_LOG_DIR      = 'logs'
DEF_NZB_DIR      = 'nzb_backup'
DEF_NZBBACK_DIR  = ''
DEF_TEMPLATES    = 'templates'
DEF_MAIN_TMPL    = 'main.tmpl'
DEF_INI_FILE     = 'sabnzbd.ini'
DEF_HOST         = '127.0.0.1'
DEF_PORT         = 8080
DEF_WORKDIR      = 'sabnzbd'
DEF_LOG_FILE     = 'sabnzbd.log'
DEF_LOG_ERRFILE  = 'sabnzbd.error.log'
DEF_LOG_CHERRY   = 'cherrypy.log'
DEF_TIMEOUT      = 120
MIN_TIMEOUT      = 30