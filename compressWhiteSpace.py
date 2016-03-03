#coding=utf-8
import re

REGEX_LINE_BREAKS = re.compile( r"\n\s*" )
REGEX_LINE_SPACE = re.compile( r"\n\s*\r" ) 
REGEX_SPACE = re.compile( r"( )+" )

'''
去除html/json/plist文件中的换行符及空白字符
'''
def compress( srcFilePath, dstFilePath ):
	srcFile = open( srcFilePath, "r" )
	srcContent = srcFile.read()
	srcContent = REGEX_LINE_BREAKS.sub( "", srcContent )
	srcContent = REGEX_LINE_SPACE.sub( "", srcContent )
	srcContent = REGEX_SPACE.sub( "", srcContent )
	srcFile.close()

	dstFile = open( dstFilePath, "w" )
	dstFile.write( srcContent )
	dstFile.close()

if __name__ == '__main__':
	compress( "spineboy.json", "spineboy2.json" )