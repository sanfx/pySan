###################################################
# Makefile for SyncQueue.
###################################################

include ${MPCMAKE_PATH}/latest/MakePythonPackage
include ${MPCMAKE_INC}/MakeShellScript

MODULE = pySan
VERSION = 0.1.0
DESCRIPTION = python package for various projects and other independent usages.
MAILTO = pipeline-support
AUTHORS = sanjeev-ku
BUILD_FOR = c5maya2011

###################################
# MakeShellScript
###################################

wrappers.SOURCES = ${call GetFiles,scripts}
wrappers.FILE_ROOT = scripts
${call MakeShellScript,wrappers}

###################################
# MakePythonPackage
###################################

python.PYTHON_ROOT = python
python.REPLACEMENTS = \
	!VERSION!=${VERSION}
${call MakePythonPackage,python}

