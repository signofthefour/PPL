# Generated from /home/nguyendat/Documents/projects/PPL/Assignments/assignment2/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2S")
        buf.write("\u02ed\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\3\2\3\2\3\2\3\2\3\2\7\2\u00cb")
        buf.write("\n\2\f\2\16\2\u00ce\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u00db\n\3\3\4\3\4\5\4\u00df\n\4\3\5")
        buf.write("\3\5\3\5\3\5\5\5\u00e5\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00ec")
        buf.write("\n\6\3\7\3\7\3\b\3\b\5\b\u00f2\n\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\5\f\u00fc\n\f\3\r\3\r\3\r\5\r\u0101\n\r")
        buf.write("\3\r\6\r\u0104\n\r\r\r\16\r\u0105\3\16\3\16\7\16\u010a")
        buf.write("\n\16\f\16\16\16\u010d\13\16\3\17\6\17\u0110\n\17\r\17")
        buf.write("\16\17\u0111\3\17\3\17\5\17\u0116\n\17\3\17\5\17\u0119")
        buf.write("\n\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\5\23\u0127\n\23\3\24\3\24\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u0131\n\26\3\26\3\26\7\26\u0135\n\26")
        buf.write("\f\26\16\26\u0138\13\26\3\27\3\27\3\27\7\27\u013d\n\27")
        buf.write("\f\27\16\27\u0140\13\27\5\27\u0142\n\27\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0148\n\30\3\30\3\30\7\30\u014c\n\30\f\30\16")
        buf.write("\30\u014f\13\30\3\31\3\31\3\31\5\31\u0154\n\31\3\32\3")
        buf.write("\32\3\33\3\33\5\33\u015a\n\33\3\34\3\34\7\34\u015e\n\34")
        buf.write("\f\34\16\34\u0161\13\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("9\39\39\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3D\3E\3E\3E\3")
        buf.write("F\3F\3F\3G\3G\3G\3G\3H\3H\3H\3H\3I\3I\3J\3J\3K\3K\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3V\3V\3V\3V\3V\3V\3W\3W\3W\3W\3W\3W\3W\3W\3W\3W\3")
        buf.write("W\3W\3W\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3X\3")
        buf.write("X\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3")
        buf.write("Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3[\3[\3[\3[\3[\3")
        buf.write("[\3[\3[\3[\3[\3[\3[\3[\3[\3\\\3\\\3\\\3\\\3\\\3\\\3\\")
        buf.write("\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3]\3]\3]\3]\7]\u02b8")
        buf.write("\n]\f]\16]\u02bb\13]\3]\3]\3]\3]\3]\3^\6^\u02c3\n^\r^")
        buf.write("\16^\u02c4\3^\3^\3_\3_\7_\u02cb\n_\f_\16_\u02ce\13_\3")
        buf.write("_\3_\3_\3`\3`\7`\u02d5\n`\f`\16`\u02d8\13`\3`\5`\u02db")
        buf.write("\n`\3`\3`\3a\3a\3a\3a\3a\3a\7a\u02e5\na\fa\16a\u02e8\13")
        buf.write("a\3a\3a\3b\3b\4\u02b9\u02e6\2c\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2")
        buf.write("%\2\'\2)\2+\2-\2/\2\61\n\63\13\65\f\67\r9\16;\17=\20?")
        buf.write("\21A\22C\23E\24G\25I\26K\27M\30O\31Q\32S\33U\34W\35Y\36")
        buf.write("[\37] _!a\"c#e$g%i&k\'m(o)q*s+u,w-y.{/}\60\177\61\u0081")
        buf.write("\62\u0083\63\u0085\64\u0087\65\u0089\66\u008b\67\u008d")
        buf.write("8\u008f9\u0091:\u0093;\u0095<\u0097=\u0099>\u009b?\u009d")
        buf.write("@\u009fA\u00a1B\u00a3C\u00a5D\u00a7E\u00a9F\u00abG\u00ad")
        buf.write("H\u00afI\u00b1J\u00b3K\u00b5L\u00b7M\u00b9N\u00bbO\u00bd")
        buf.write("P\u00bfQ\u00c1R\u00c3S\3\2\22\3\2c|\3\2C\\\3\2\62;\4\2")
        buf.write("GGgg\3\2\60\60\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\4")
        buf.write("\2\62;CH\3\2\629\4\2\63;CH\3\2\62\62\3\2\63;\3\2\639\5")
        buf.write("\2\13\f\16\17\"\"\4\3\n\f\16\17\3\2,,\2\u030d\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2")
        buf.write("\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf")
        buf.write("\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\3\u00c5\3\2\2")
        buf.write("\2\5\u00da\3\2\2\2\7\u00de\3\2\2\2\t\u00e4\3\2\2\2\13")
        buf.write("\u00eb\3\2\2\2\r\u00ed\3\2\2\2\17\u00f1\3\2\2\2\21\u00f3")
        buf.write("\3\2\2\2\23\u00f5\3\2\2\2\25\u00f7\3\2\2\2\27\u00fb\3")
        buf.write("\2\2\2\31\u00fd\3\2\2\2\33\u0107\3\2\2\2\35\u010f\3\2")
        buf.write("\2\2\37\u011a\3\2\2\2!\u011d\3\2\2\2#\u0120\3\2\2\2%\u0126")
        buf.write("\3\2\2\2\'\u0128\3\2\2\2)\u012a\3\2\2\2+\u0130\3\2\2\2")
        buf.write("-\u0141\3\2\2\2/\u0147\3\2\2\2\61\u0153\3\2\2\2\63\u0155")
        buf.write("\3\2\2\2\65\u0159\3\2\2\2\67\u015b\3\2\2\29\u0165\3\2")
        buf.write("\2\2;\u016a\3\2\2\2=\u0170\3\2\2\2?\u0179\3\2\2\2A\u017c")
        buf.write("\3\2\2\2C\u0181\3\2\2\2E\u0188\3\2\2\2G\u018e\3\2\2\2")
        buf.write("I\u0196\3\2\2\2K\u019d\3\2\2\2M\u01a6\3\2\2\2O\u01aa\3")
        buf.write("\2\2\2Q\u01b3\3\2\2\2S\u01b6\3\2\2\2U\u01c0\3\2\2\2W\u01c7")
        buf.write("\3\2\2\2Y\u01cc\3\2\2\2[\u01d0\3\2\2\2]\u01d6\3\2\2\2")
        buf.write("_\u01db\3\2\2\2a\u01e1\3\2\2\2c\u01e7\3\2\2\2e\u01e9\3")
        buf.write("\2\2\2g\u01ec\3\2\2\2i\u01ee\3\2\2\2k\u01f1\3\2\2\2m\u01f3")
        buf.write("\3\2\2\2o\u01f6\3\2\2\2q\u01f8\3\2\2\2s\u01fb\3\2\2\2")
        buf.write("u\u01fd\3\2\2\2w\u01ff\3\2\2\2y\u0202\3\2\2\2{\u0205\3")
        buf.write("\2\2\2}\u0208\3\2\2\2\177\u020b\3\2\2\2\u0081\u020d\3")
        buf.write("\2\2\2\u0083\u020f\3\2\2\2\u0085\u0212\3\2\2\2\u0087\u0215")
        buf.write("\3\2\2\2\u0089\u0219\3\2\2\2\u008b\u021c\3\2\2\2\u008d")
        buf.write("\u021f\3\2\2\2\u008f\u0223\3\2\2\2\u0091\u0227\3\2\2\2")
        buf.write("\u0093\u0229\3\2\2\2\u0095\u022b\3\2\2\2\u0097\u022d\3")
        buf.write("\2\2\2\u0099\u022f\3\2\2\2\u009b\u0231\3\2\2\2\u009d\u0233")
        buf.write("\3\2\2\2\u009f\u0235\3\2\2\2\u00a1\u0237\3\2\2\2\u00a3")
        buf.write("\u0239\3\2\2\2\u00a5\u023b\3\2\2\2\u00a7\u023d\3\2\2\2")
        buf.write("\u00a9\u023f\3\2\2\2\u00ab\u024c\3\2\2\2\u00ad\u025a\3")
        buf.write("\2\2\2\u00af\u0267\3\2\2\2\u00b1\u0277\3\2\2\2\u00b3\u0286")
        buf.write("\3\2\2\2\u00b5\u0295\3\2\2\2\u00b7\u02a3\3\2\2\2\u00b9")
        buf.write("\u02b3\3\2\2\2\u00bb\u02c2\3\2\2\2\u00bd\u02c8\3\2\2\2")
        buf.write("\u00bf\u02d2\3\2\2\2\u00c1\u02de\3\2\2\2\u00c3\u02eb\3")
        buf.write("\2\2\2\u00c5\u00cc\5\21\t\2\u00c6\u00cb\5\21\t\2\u00c7")
        buf.write("\u00cb\5\25\13\2\u00c8\u00cb\5\23\n\2\u00c9\u00cb\7a\2")
        buf.write("\2\u00ca\u00c6\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\4\3\2\2\2\u00ce")
        buf.write("\u00cc\3\2\2\2\u00cf\u00db\5{>\2\u00d0\u00db\5}?\2\u00d1")
        buf.write("\u00db\5\177@\2\u00d2\u00db\5\u0081A\2\u00d3\u00db\5\u0083")
        buf.write("B\2\u00d4\u00db\5\u0085C\2\u00d5\u00db\5\u0087D\2\u00d6")
        buf.write("\u00db\5\u0089E\2\u00d7\u00db\5\u008bF\2\u00d8\u00db\5")
        buf.write("\u008dG\2\u00d9\u00db\5\u008fH\2\u00da\u00cf\3\2\2\2\u00da")
        buf.write("\u00d0\3\2\2\2\u00da\u00d1\3\2\2\2\u00da\u00d2\3\2\2\2")
        buf.write("\u00da\u00d3\3\2\2\2\u00da\u00d4\3\2\2\2\u00da\u00d5\3")
        buf.write("\2\2\2\u00da\u00d6\3\2\2\2\u00da\u00d7\3\2\2\2\u00da\u00d8")
        buf.write("\3\2\2\2\u00da\u00d9\3\2\2\2\u00db\6\3\2\2\2\u00dc\u00df")
        buf.write("\5w<\2\u00dd\u00df\5y=\2\u00de\u00dc\3\2\2\2\u00de\u00dd")
        buf.write("\3\2\2\2\u00df\b\3\2\2\2\u00e0\u00e5\5e\63\2\u00e1\u00e5")
        buf.write("\5c\62\2\u00e2\u00e5\5i\65\2\u00e3\u00e5\5g\64\2\u00e4")
        buf.write("\u00e0\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e3\3\2\2\2\u00e5\n\3\2\2\2\u00e6\u00ec\5k\66")
        buf.write("\2\u00e7\u00ec\5m\67\2\u00e8\u00ec\5q9\2\u00e9\u00ec\5")
        buf.write("o8\2\u00ea\u00ec\5s:\2\u00eb\u00e6\3\2\2\2\u00eb\u00e7")
        buf.write("\3\2\2\2\u00eb\u00e8\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\f\3\2\2\2\u00ed\u00ee\5u;\2\u00ee")
        buf.write("\16\3\2\2\2\u00ef\u00f2\5i\65\2\u00f0\u00f2\5g\64\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\20\3\2\2\2\u00f3")
        buf.write("\u00f4\t\2\2\2\u00f4\22\3\2\2\2\u00f5\u00f6\t\3\2\2\u00f6")
        buf.write("\24\3\2\2\2\u00f7\u00f8\t\4\2\2\u00f8\26\3\2\2\2\u00f9")
        buf.write("\u00fc\5\21\t\2\u00fa\u00fc\5\23\n\2\u00fb\u00f9\3\2\2")
        buf.write("\2\u00fb\u00fa\3\2\2\2\u00fc\30\3\2\2\2\u00fd\u0100\t")
        buf.write("\5\2\2\u00fe\u0101\5g\64\2\u00ff\u0101\5c\62\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0103\3\2\2\2\u0102\u0104\5\25\13\2\u0103\u0102\3\2\2")
        buf.write("\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106\32\3\2\2\2\u0107\u010b\t\6\2\2\u0108\u010a")
        buf.write("\5\25\13\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\34\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010e\u0110\5\25\13\2\u010f\u010e\3\2\2")
        buf.write("\2\u0110\u0111\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\u0118\3\2\2\2\u0113\u0115\5\33\16\2\u0114")
        buf.write("\u0116\5\31\r\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2")
        buf.write("\2\u0116\u0119\3\2\2\2\u0117\u0119\5\31\r\2\u0118\u0113")
        buf.write("\3\2\2\2\u0118\u0117\3\2\2\2\u0119\36\3\2\2\2\u011a\u011b")
        buf.write("\7^\2\2\u011b\u011c\n\7\2\2\u011c \3\2\2\2\u011d\u011e")
        buf.write("\7^\2\2\u011e\u011f\t\7\2\2\u011f\"\3\2\2\2\u0120\u0121")
        buf.write("\7)\2\2\u0121\u0122\7$\2\2\u0122$\3\2\2\2\u0123\u0127")
        buf.write("\n\b\2\2\u0124\u0127\5!\21\2\u0125\u0127\5#\22\2\u0126")
        buf.write("\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127&\3\2\2\2\u0128\u0129\t\t\2\2\u0129(\3\2\2\2\u012a")
        buf.write("\u012b\t\n\2\2\u012b*\3\2\2\2\u012c\u012d\7\62\2\2\u012d")
        buf.write("\u0131\7z\2\2\u012e\u012f\7\62\2\2\u012f\u0131\7Z\2\2")
        buf.write("\u0130\u012c\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132\3")
        buf.write("\2\2\2\u0132\u0136\t\13\2\2\u0133\u0135\5\'\24\2\u0134")
        buf.write("\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2")
        buf.write("\u0136\u0137\3\2\2\2\u0137,\3\2\2\2\u0138\u0136\3\2\2")
        buf.write("\2\u0139\u0142\t\f\2\2\u013a\u013e\t\r\2\2\u013b\u013d")
        buf.write("\t\4\2\2\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0142\3\2\2\2")
        buf.write("\u0140\u013e\3\2\2\2\u0141\u0139\3\2\2\2\u0141\u013a\3")
        buf.write("\2\2\2\u0142.\3\2\2\2\u0143\u0144\7\62\2\2\u0144\u0148")
        buf.write("\7q\2\2\u0145\u0146\7\62\2\2\u0146\u0148\7Q\2\2\u0147")
        buf.write("\u0143\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014d\t\16\2\2\u014a\u014c\5)\25\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\60\3\2\2\2\u014f\u014d\3\2\2\2\u0150")
        buf.write("\u0154\5-\27\2\u0151\u0154\5+\26\2\u0152\u0154\5/\30\2")
        buf.write("\u0153\u0150\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0152\3")
        buf.write("\2\2\2\u0154\62\3\2\2\2\u0155\u0156\5\35\17\2\u0156\64")
        buf.write("\3\2\2\2\u0157\u015a\5]/\2\u0158\u015a\5_\60\2\u0159\u0157")
        buf.write("\3\2\2\2\u0159\u0158\3\2\2\2\u015a\66\3\2\2\2\u015b\u015f")
        buf.write("\5\u00a7T\2\u015c\u015e\5%\23\2\u015d\u015c\3\2\2\2\u015e")
        buf.write("\u0161\3\2\2\2\u015f\u015d\3\2\2\2\u015f\u0160\3\2\2\2")
        buf.write("\u0160\u0162\3\2\2\2\u0161\u015f\3\2\2\2\u0162\u0163\5")
        buf.write("\u00a7T\2\u0163\u0164\b\34\2\2\u01648\3\2\2\2\u0165\u0166")
        buf.write("\7D\2\2\u0166\u0167\7q\2\2\u0167\u0168\7f\2\2\u0168\u0169")
        buf.write("\7{\2\2\u0169:\3\2\2\2\u016a\u016b\7D\2\2\u016b\u016c")
        buf.write("\7t\2\2\u016c\u016d\7g\2\2\u016d\u016e\7c\2\2\u016e\u016f")
        buf.write("\7m\2\2\u016f<\3\2\2\2\u0170\u0171\7E\2\2\u0171\u0172")
        buf.write("\7q\2\2\u0172\u0173\7p\2\2\u0173\u0174\7v\2\2\u0174\u0175")
        buf.write("\7k\2\2\u0175\u0176\7p\2\2\u0176\u0177\7w\2\2\u0177\u0178")
        buf.write("\7g\2\2\u0178>\3\2\2\2\u0179\u017a\7F\2\2\u017a\u017b")
        buf.write("\7q\2\2\u017b@\3\2\2\2\u017c\u017d\7G\2\2\u017d\u017e")
        buf.write("\7n\2\2\u017e\u017f\7u\2\2\u017f\u0180\7g\2\2\u0180B\3")
        buf.write("\2\2\2\u0181\u0182\7G\2\2\u0182\u0183\7n\2\2\u0183\u0184")
        buf.write("\7u\2\2\u0184\u0185\7g\2\2\u0185\u0186\7K\2\2\u0186\u0187")
        buf.write("\7h\2\2\u0187D\3\2\2\2\u0188\u0189\7G\2\2\u0189\u018a")
        buf.write("\7p\2\2\u018a\u018b\7f\2\2\u018b\u018c\7K\2\2\u018c\u018d")
        buf.write("\7h\2\2\u018dF\3\2\2\2\u018e\u018f\7G\2\2\u018f\u0190")
        buf.write("\7p\2\2\u0190\u0191\7f\2\2\u0191\u0192\7D\2\2\u0192\u0193")
        buf.write("\7q\2\2\u0193\u0194\7f\2\2\u0194\u0195\7{\2\2\u0195H\3")
        buf.write("\2\2\2\u0196\u0197\7G\2\2\u0197\u0198\7p\2\2\u0198\u0199")
        buf.write("\7f\2\2\u0199\u019a\7H\2\2\u019a\u019b\7q\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019cJ\3\2\2\2\u019d\u019e\7G\2\2\u019e\u019f")
        buf.write("\7p\2\2\u019f\u01a0\7f\2\2\u01a0\u01a1\7Y\2\2\u01a1\u01a2")
        buf.write("\7j\2\2\u01a2\u01a3\7k\2\2\u01a3\u01a4\7n\2\2\u01a4\u01a5")
        buf.write("\7g\2\2\u01a5L\3\2\2\2\u01a6\u01a7\7H\2\2\u01a7\u01a8")
        buf.write("\7q\2\2\u01a8\u01a9\7t\2\2\u01a9N\3\2\2\2\u01aa\u01ab")
        buf.write("\7H\2\2\u01ab\u01ac\7w\2\2\u01ac\u01ad\7p\2\2\u01ad\u01ae")
        buf.write("\7e\2\2\u01ae\u01af\7v\2\2\u01af\u01b0\7k\2\2\u01b0\u01b1")
        buf.write("\7q\2\2\u01b1\u01b2\7p\2\2\u01b2P\3\2\2\2\u01b3\u01b4")
        buf.write("\7K\2\2\u01b4\u01b5\7h\2\2\u01b5R\3\2\2\2\u01b6\u01b7")
        buf.write("\7R\2\2\u01b7\u01b8\7c\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba")
        buf.write("\7c\2\2\u01ba\u01bb\7o\2\2\u01bb\u01bc\7g\2\2\u01bc\u01bd")
        buf.write("\7v\2\2\u01bd\u01be\7g\2\2\u01be\u01bf\7t\2\2\u01bfT\3")
        buf.write("\2\2\2\u01c0\u01c1\7T\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3")
        buf.write("\7v\2\2\u01c3\u01c4\7w\2\2\u01c4\u01c5\7t\2\2\u01c5\u01c6")
        buf.write("\7p\2\2\u01c6V\3\2\2\2\u01c7\u01c8\7V\2\2\u01c8\u01c9")
        buf.write("\7j\2\2\u01c9\u01ca\7g\2\2\u01ca\u01cb\7p\2\2\u01cbX\3")
        buf.write("\2\2\2\u01cc\u01cd\7X\2\2\u01cd\u01ce\7c\2\2\u01ce\u01cf")
        buf.write("\7t\2\2\u01cfZ\3\2\2\2\u01d0\u01d1\7Y\2\2\u01d1\u01d2")
        buf.write("\7j\2\2\u01d2\u01d3\7k\2\2\u01d3\u01d4\7n\2\2\u01d4\u01d5")
        buf.write("\7g\2\2\u01d5\\\3\2\2\2\u01d6\u01d7\7V\2\2\u01d7\u01d8")
        buf.write("\7t\2\2\u01d8\u01d9\7w\2\2\u01d9\u01da\7g\2\2\u01da^\3")
        buf.write("\2\2\2\u01db\u01dc\7H\2\2\u01dc\u01dd\7c\2\2\u01dd\u01de")
        buf.write("\7n\2\2\u01de\u01df\7u\2\2\u01df\u01e0\7g\2\2\u01e0`\3")
        buf.write("\2\2\2\u01e1\u01e2\7G\2\2\u01e2\u01e3\7p\2\2\u01e3\u01e4")
        buf.write("\7f\2\2\u01e4\u01e5\7F\2\2\u01e5\u01e6\7q\2\2\u01e6b\3")
        buf.write("\2\2\2\u01e7\u01e8\7-\2\2\u01e8d\3\2\2\2\u01e9\u01ea\7")
        buf.write("-\2\2\u01ea\u01eb\7\60\2\2\u01ebf\3\2\2\2\u01ec\u01ed")
        buf.write("\7/\2\2\u01edh\3\2\2\2\u01ee\u01ef\7/\2\2\u01ef\u01f0")
        buf.write("\7\60\2\2\u01f0j\3\2\2\2\u01f1\u01f2\7,\2\2\u01f2l\3\2")
        buf.write("\2\2\u01f3\u01f4\7,\2\2\u01f4\u01f5\7\60\2\2\u01f5n\3")
        buf.write("\2\2\2\u01f6\u01f7\7^\2\2\u01f7p\3\2\2\2\u01f8\u01f9\7")
        buf.write("^\2\2\u01f9\u01fa\7\60\2\2\u01far\3\2\2\2\u01fb\u01fc")
        buf.write("\7\'\2\2\u01fct\3\2\2\2\u01fd\u01fe\7#\2\2\u01fev\3\2")
        buf.write("\2\2\u01ff\u0200\7(\2\2\u0200\u0201\7(\2\2\u0201x\3\2")
        buf.write("\2\2\u0202\u0203\7~\2\2\u0203\u0204\7~\2\2\u0204z\3\2")
        buf.write("\2\2\u0205\u0206\7?\2\2\u0206\u0207\7?\2\2\u0207|\3\2")
        buf.write("\2\2\u0208\u0209\7#\2\2\u0209\u020a\7?\2\2\u020a~\3\2")
        buf.write("\2\2\u020b\u020c\7>\2\2\u020c\u0080\3\2\2\2\u020d\u020e")
        buf.write("\7@\2\2\u020e\u0082\3\2\2\2\u020f\u0210\7>\2\2\u0210\u0211")
        buf.write("\7?\2\2\u0211\u0084\3\2\2\2\u0212\u0213\7@\2\2\u0213\u0214")
        buf.write("\7?\2\2\u0214\u0086\3\2\2\2\u0215\u0216\7?\2\2\u0216\u0217")
        buf.write("\7\61\2\2\u0217\u0218\7?\2\2\u0218\u0088\3\2\2\2\u0219")
        buf.write("\u021a\7>\2\2\u021a\u021b\7\60\2\2\u021b\u008a\3\2\2\2")
        buf.write("\u021c\u021d\7@\2\2\u021d\u021e\7\60\2\2\u021e\u008c\3")
        buf.write("\2\2\2\u021f\u0220\7>\2\2\u0220\u0221\7?\2\2\u0221\u0222")
        buf.write("\7\60\2\2\u0222\u008e\3\2\2\2\u0223\u0224\7@\2\2\u0224")
        buf.write("\u0225\7?\2\2\u0225\u0226\7\60\2\2\u0226\u0090\3\2\2\2")
        buf.write("\u0227\u0228\7*\2\2\u0228\u0092\3\2\2\2\u0229\u022a\7")
        buf.write("+\2\2\u022a\u0094\3\2\2\2\u022b\u022c\7]\2\2\u022c\u0096")
        buf.write("\3\2\2\2\u022d\u022e\7_\2\2\u022e\u0098\3\2\2\2\u022f")
        buf.write("\u0230\7}\2\2\u0230\u009a\3\2\2\2\u0231\u0232\7\177\2")
        buf.write("\2\u0232\u009c\3\2\2\2\u0233\u0234\7<\2\2\u0234\u009e")
        buf.write("\3\2\2\2\u0235\u0236\7\60\2\2\u0236\u00a0\3\2\2\2\u0237")
        buf.write("\u0238\7=\2\2\u0238\u00a2\3\2\2\2\u0239\u023a\7.\2\2\u023a")
        buf.write("\u00a4\3\2\2\2\u023b\u023c\7?\2\2\u023c\u00a6\3\2\2\2")
        buf.write("\u023d\u023e\7$\2\2\u023e\u00a8\3\2\2\2\u023f\u0240\7")
        buf.write("k\2\2\u0240\u0241\7p\2\2\u0241\u0242\7v\2\2\u0242\u0243")
        buf.write("\7a\2\2\u0243\u0244\7q\2\2\u0244\u0245\7h\2\2\u0245\u0246")
        buf.write("\7a\2\2\u0246\u0247\7h\2\2\u0247\u0248\7n\2\2\u0248\u0249")
        buf.write("\7q\2\2\u0249\u024a\7c\2\2\u024a\u024b\7v\2\2\u024b\u00aa")
        buf.write("\3\2\2\2\u024c\u024d\7k\2\2\u024d\u024e\7p\2\2\u024e\u024f")
        buf.write("\7v\2\2\u024f\u0250\7a\2\2\u0250\u0251\7q\2\2\u0251\u0252")
        buf.write("\7h\2\2\u0252\u0253\7a\2\2\u0253\u0254\7u\2\2\u0254\u0255")
        buf.write("\7v\2\2\u0255\u0256\7t\2\2\u0256\u0257\7k\2\2\u0257\u0258")
        buf.write("\7p\2\2\u0258\u0259\7i\2\2\u0259\u00ac\3\2\2\2\u025a\u025b")
        buf.write("\7h\2\2\u025b\u025c\7n\2\2\u025c\u025d\7q\2\2\u025d\u025e")
        buf.write("\7c\2\2\u025e\u025f\7v\2\2\u025f\u0260\7a\2\2\u0260\u0261")
        buf.write("\7v\2\2\u0261\u0262\7q\2\2\u0262\u0263\7a\2\2\u0263\u0264")
        buf.write("\7k\2\2\u0264\u0265\7p\2\2\u0265\u0266\7v\2\2\u0266\u00ae")
        buf.write("\3\2\2\2\u0267\u0268\7h\2\2\u0268\u0269\7n\2\2\u0269\u026a")
        buf.write("\7q\2\2\u026a\u026b\7c\2\2\u026b\u026c\7v\2\2\u026c\u026d")
        buf.write("\7a\2\2\u026d\u026e\7q\2\2\u026e\u026f\7h\2\2\u026f\u0270")
        buf.write("\7a\2\2\u0270\u0271\7u\2\2\u0271\u0272\7v\2\2\u0272\u0273")
        buf.write("\7t\2\2\u0273\u0274\7k\2\2\u0274\u0275\7p\2\2\u0275\u0276")
        buf.write("\7i\2\2\u0276\u00b0\3\2\2\2\u0277\u0278\7d\2\2\u0278\u0279")
        buf.write("\7q\2\2\u0279\u027a\7q\2\2\u027a\u027b\7n\2\2\u027b\u027c")
        buf.write("\7a\2\2\u027c\u027d\7q\2\2\u027d\u027e\7h\2\2\u027e\u027f")
        buf.write("\7a\2\2\u027f\u0280\7u\2\2\u0280\u0281\7v\2\2\u0281\u0282")
        buf.write("\7t\2\2\u0282\u0283\7k\2\2\u0283\u0284\7p\2\2\u0284\u0285")
        buf.write("\7i\2\2\u0285\u00b2\3\2\2\2\u0286\u0287\7u\2\2\u0287\u0288")
        buf.write("\7v\2\2\u0288\u0289\7t\2\2\u0289\u028a\7k\2\2\u028a\u028b")
        buf.write("\7p\2\2\u028b\u028c\7i\2\2\u028c\u028d\7a\2\2\u028d\u028e")
        buf.write("\7q\2\2\u028e\u028f\7h\2\2\u028f\u0290\7a\2\2\u0290\u0291")
        buf.write("\7d\2\2\u0291\u0292\7q\2\2\u0292\u0293\7q\2\2\u0293\u0294")
        buf.write("\7n\2\2\u0294\u00b4\3\2\2\2\u0295\u0296\7u\2\2\u0296\u0297")
        buf.write("\7v\2\2\u0297\u0298\7t\2\2\u0298\u0299\7k\2\2\u0299\u029a")
        buf.write("\7p\2\2\u029a\u029b\7i\2\2\u029b\u029c\7a\2\2\u029c\u029d")
        buf.write("\7q\2\2\u029d\u029e\7h\2\2\u029e\u029f\7a\2\2\u029f\u02a0")
        buf.write("\7k\2\2\u02a0\u02a1\7p\2\2\u02a1\u02a2\7v\2\2\u02a2\u00b6")
        buf.write("\3\2\2\2\u02a3\u02a4\7u\2\2\u02a4\u02a5\7v\2\2\u02a5\u02a6")
        buf.write("\7t\2\2\u02a6\u02a7\7k\2\2\u02a7\u02a8\7p\2\2\u02a8\u02a9")
        buf.write("\7i\2\2\u02a9\u02aa\7a\2\2\u02aa\u02ab\7q\2\2\u02ab\u02ac")
        buf.write("\7h\2\2\u02ac\u02ad\7a\2\2\u02ad\u02ae\7h\2\2\u02ae\u02af")
        buf.write("\7n\2\2\u02af\u02b0\7q\2\2\u02b0\u02b1\7c\2\2\u02b1\u02b2")
        buf.write("\7v\2\2\u02b2\u00b8\3\2\2\2\u02b3\u02b4\7,\2\2\u02b4\u02b5")
        buf.write("\7,\2\2\u02b5\u02b9\3\2\2\2\u02b6\u02b8\13\2\2\2\u02b7")
        buf.write("\u02b6\3\2\2\2\u02b8\u02bb\3\2\2\2\u02b9\u02ba\3\2\2\2")
        buf.write("\u02b9\u02b7\3\2\2\2\u02ba\u02bc\3\2\2\2\u02bb\u02b9\3")
        buf.write("\2\2\2\u02bc\u02bd\7,\2\2\u02bd\u02be\7,\2\2\u02be\u02bf")
        buf.write("\3\2\2\2\u02bf\u02c0\b]\3\2\u02c0\u00ba\3\2\2\2\u02c1")
        buf.write("\u02c3\t\17\2\2\u02c2\u02c1\3\2\2\2\u02c3\u02c4\3\2\2")
        buf.write("\2\u02c4\u02c2\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5\u02c6")
        buf.write("\3\2\2\2\u02c6\u02c7\b^\3\2\u02c7\u00bc\3\2\2\2\u02c8")
        buf.write("\u02cc\7$\2\2\u02c9\u02cb\5%\23\2\u02ca\u02c9\3\2\2\2")
        buf.write("\u02cb\u02ce\3\2\2\2\u02cc\u02ca\3\2\2\2\u02cc\u02cd\3")
        buf.write("\2\2\2\u02cd\u02cf\3\2\2\2\u02ce\u02cc\3\2\2\2\u02cf\u02d0")
        buf.write("\5\37\20\2\u02d0\u02d1\b_\4\2\u02d1\u00be\3\2\2\2\u02d2")
        buf.write("\u02d6\7$\2\2\u02d3\u02d5\5%\23\2\u02d4\u02d3\3\2\2\2")
        buf.write("\u02d5\u02d8\3\2\2\2\u02d6\u02d4\3\2\2\2\u02d6\u02d7\3")
        buf.write("\2\2\2\u02d7\u02da\3\2\2\2\u02d8\u02d6\3\2\2\2\u02d9\u02db")
        buf.write("\t\20\2\2\u02da\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc")
        buf.write("\u02dd\b`\5\2\u02dd\u00c0\3\2\2\2\u02de\u02df\7,\2\2\u02df")
        buf.write("\u02e0\7,\2\2\u02e0\u02e6\3\2\2\2\u02e1\u02e2\7,\2\2\u02e2")
        buf.write("\u02e5\n\21\2\2\u02e3\u02e5\n\21\2\2\u02e4\u02e1\3\2\2")
        buf.write("\2\u02e4\u02e3\3\2\2\2\u02e5\u02e8\3\2\2\2\u02e6\u02e7")
        buf.write("\3\2\2\2\u02e6\u02e4\3\2\2\2\u02e7\u02e9\3\2\2\2\u02e8")
        buf.write("\u02e6\3\2\2\2\u02e9\u02ea\7\2\2\3\u02ea\u00c2\3\2\2\2")
        buf.write("\u02eb\u02ec\13\2\2\2\u02ec\u00c4\3\2\2\2\"\2\u00ca\u00cc")
        buf.write("\u00da\u00de\u00e4\u00eb\u00f1\u00fb\u0100\u0105\u010b")
        buf.write("\u0111\u0115\u0118\u0126\u0130\u0136\u013e\u0141\u0147")
        buf.write("\u014d\u0153\u0159\u015f\u02b9\u02c4\u02cc\u02d6\u02da")
        buf.write("\u02e4\u02e6\6\3\34\2\b\2\2\3_\3\3`\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    REL_OP = 2
    BIN_LOGICAL_OP = 3
    ADD_OP = 4
    MUL_OP = 5
    UN_LOGICAL_OP = 6
    UN_OP = 7
    INT_LIT = 8
    FLOAT_LIT = 9
    BOOL_LIT = 10
    STRING_LIT = 11
    BODY = 12
    BREAK = 13
    CONTINUE = 14
    DO = 15
    ELSE = 16
    ELSEIF = 17
    ENDIF = 18
    ENDBODY = 19
    ENDFOR = 20
    ENDWHILE = 21
    FOR = 22
    FUNCTION = 23
    IF = 24
    PARAMETER = 25
    RETURN = 26
    THEN = 27
    VAR = 28
    WHILE = 29
    TRUE = 30
    FALSE = 31
    ENDDO = 32
    PLUS_INT = 33
    PLUS_FLOAT = 34
    MINUS_INT = 35
    MINUS_FLOAT = 36
    STAR_INT = 37
    STAR_FLOAT = 38
    DIV_INT = 39
    DIV_FLOAT = 40
    MOD = 41
    NOT = 42
    AND = 43
    OR = 44
    EQUAL = 45
    NOT_EQUAL_INT = 46
    LESS_INT = 47
    GREATER_INT = 48
    LESS_OR_EQUAL_INT = 49
    GREATER_OR_EQUAL_INT = 50
    NOT_EQUAL_FLOAT = 51
    LESS_FLOAT = 52
    GREATER_FLOAT = 53
    LESS_OR_EQUAL_FLOAT = 54
    GREATER_OR_EQUAL_FLOAT = 55
    LEFT_PAREN = 56
    RIGHT_PAREN = 57
    LEFT_BRACKET = 58
    RIGHT_BRACKET = 59
    LEFT_BRACE = 60
    RIGHT_BRACE = 61
    COLON = 62
    DOT = 63
    SEMI = 64
    COMMA = 65
    ASSIGN = 66
    DOUBLE_QUOTE = 67
    INT_OF_FLOAT = 68
    INT_OF_STRING = 69
    FLOAT_TO_INT = 70
    FLOAT_OF_STRING = 71
    BOOL_OF_STRING = 72
    STRING_OF_BOOL = 73
    STRING_OF_INT = 74
    STRING_OF_FLOAT = 75
    COMMENT = 76
    WS = 77
    ILLEGAL_ESCAPE = 78
    UNCLOSE_STRING = 79
    UNTERMINATED_COMMENT = 80
    ERROR_CHAR = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndIf'", "'EndBody'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "':'", "'.'", "';'", "','", "'='", "'\"'", "'int_of_float'", 
            "'int_of_string'", "'float_to_int'", "'float_of_string'", "'bool_of_string'", 
            "'string_of_bool'", "'string_of_int'", "'string_of_float'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "REL_OP", "BIN_LOGICAL_OP", "ADD_OP", "MUL_OP", "UN_LOGICAL_OP", 
            "UN_OP", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "BODY", 
            "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", 
            "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", 
            "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", 
            "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
            "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
            "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
            "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "DOUBLE_QUOTE", 
            "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_TO_INT", "FLOAT_OF_STRING", 
            "BOOL_OF_STRING", "STRING_OF_BOOL", "STRING_OF_INT", "STRING_OF_FLOAT", 
            "COMMENT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR" ]

    ruleNames = [ "ID", "REL_OP", "BIN_LOGICAL_OP", "ADD_OP", "MUL_OP", 
                  "UN_LOGICAL_OP", "UN_OP", "LOWERCASE_LETTER", "UPPERCASE_LETTER", 
                  "DIGIT", "LETTER", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
                  "ILL_ESC_SEQUENCE", "SUP_ESC_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", 
                  "STRING_CHAR", "HEXADECIMALDIGIT", "OCTALDIGIT", "HEXADECIMAL", 
                  "DECIMAL", "OCTAL", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
                  "STRING_LIT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
                  "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", 
                  "MINUS_INT", "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", 
                  "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", 
                  "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", 
                  "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", 
                  "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", 
                  "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "LEFT_BRACE", "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", 
                  "ASSIGN", "DOUBLE_QUOTE", "INT_OF_FLOAT", "INT_OF_STRING", 
                  "FLOAT_TO_INT", "FLOAT_OF_STRING", "BOOL_OF_STRING", "STRING_OF_BOOL", 
                  "STRING_OF_INT", "STRING_OF_FLOAT", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[26] = self.STRING_LIT_action 
            actions[93] = self.ILLEGAL_ESCAPE_action 
            actions[94] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    self.text = y[1:]
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    y = str(self.text)
                    self.text = y[1:]
                
     


