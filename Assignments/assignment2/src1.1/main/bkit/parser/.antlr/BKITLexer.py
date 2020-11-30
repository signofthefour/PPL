# Generated from /home/nguyendat/Documents/projects/PPL/Assignments/assignment2/src1.1/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2M")
        buf.write("\u02bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2")
        buf.write("\3\2\3\2\3\2\7\2\u00bf\n\2\f\2\16\2\u00c2\13\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\5\6\u00cc\n\6\3\7\3\7\3\7\5\7")
        buf.write("\u00d1\n\7\3\7\6\7\u00d4\n\7\r\7\16\7\u00d5\3\b\3\b\7")
        buf.write("\b\u00da\n\b\f\b\16\b\u00dd\13\b\3\t\6\t\u00e0\n\t\r\t")
        buf.write("\16\t\u00e1\3\t\3\t\5\t\u00e6\n\t\3\t\5\t\u00e9\n\t\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\5\r")
        buf.write("\u00f7\n\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u0101\n\20\3\20\3\20\7\20\u0105\n\20\f\20\16\20\u0108")
        buf.write("\13\20\3\21\3\21\3\21\7\21\u010d\n\21\f\21\16\21\u0110")
        buf.write("\13\21\5\21\u0112\n\21\3\22\3\22\3\22\3\22\5\22\u0118")
        buf.write("\n\22\3\22\3\22\7\22\u011c\n\22\f\22\16\22\u011f\13\22")
        buf.write("\3\23\3\23\3\23\5\23\u0124\n\23\3\24\3\24\3\25\3\25\5")
        buf.write("\25\u012a\n\25\3\26\3\26\7\26\u012e\n\26\f\26\16\26\u0131")
        buf.write("\13\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(")
        buf.write("\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3<")
        buf.write("\3<\3<\3=\3=\3=\3>\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3")
        buf.write("I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\3O\3O\3O\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3P\3")
        buf.write("P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3R\3R\3")
        buf.write("R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3")
        buf.write("S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3T\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\3T\3T\3T\3U\3U\3U\3U\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3V\3")
        buf.write("V\3V\3W\3W\3W\3W\7W\u0288\nW\fW\16W\u028b\13W\3W\3W\3")
        buf.write("W\3W\3W\3X\6X\u0293\nX\rX\16X\u0294\3X\3X\3Y\3Y\7Y\u029b")
        buf.write("\nY\fY\16Y\u029e\13Y\3Y\3Y\3Y\3Z\3Z\7Z\u02a5\nZ\fZ\16")
        buf.write("Z\u02a8\13Z\3Z\5Z\u02ab\nZ\3Z\3Z\3[\3[\3[\3[\3[\3[\7[")
        buf.write("\u02b5\n[\f[\16[\u02b8\13[\3[\3[\3\\\3\\\4\u0289\u02b6")
        buf.write("\2]\3\3\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\4\'\5)\6+\7-\b/\t\61\n\63")
        buf.write("\13\65\f\67\r9\16;\17=\20?\21A\22C\23E\24G\25I\26K\27")
        buf.write("M\30O\31Q\32S\33U\34W\35Y\36[\37] _!a\"c#e$g%i&k\'m(o")
        buf.write(")q*s+u,w-y.{/}\60\177\61\u0081\62\u0083\63\u0085\64\u0087")
        buf.write("\65\u0089\66\u008b\67\u008d8\u008f9\u0091:\u0093;\u0095")
        buf.write("<\u0097=\u0099>\u009b?\u009d@\u009fA\u00a1B\u00a3C\u00a5")
        buf.write("D\u00a7E\u00a9F\u00abG\u00adH\u00afI\u00b1J\u00b3K\u00b5")
        buf.write("L\u00b7M\3\2\22\3\2c|\3\2C\\\3\2\62;\4\2GGgg\3\2\60\60")
        buf.write("\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\4\2\62;CH\3\2\62")
        buf.write("9\4\2\63;CH\3\2\62\62\3\2\63;\3\2\639\5\2\13\f\16\17\"")
        buf.write("\"\4\3\n\f\16\17\3\2,,\2\u02ca\2\3\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\3\u00b9\3\2\2\2\5\u00c3")
        buf.write("\3\2\2\2\7\u00c5\3\2\2\2\t\u00c7\3\2\2\2\13\u00cb\3\2")
        buf.write("\2\2\r\u00cd\3\2\2\2\17\u00d7\3\2\2\2\21\u00df\3\2\2\2")
        buf.write("\23\u00ea\3\2\2\2\25\u00ed\3\2\2\2\27\u00f0\3\2\2\2\31")
        buf.write("\u00f6\3\2\2\2\33\u00f8\3\2\2\2\35\u00fa\3\2\2\2\37\u0100")
        buf.write("\3\2\2\2!\u0111\3\2\2\2#\u0117\3\2\2\2%\u0123\3\2\2\2")
        buf.write("\'\u0125\3\2\2\2)\u0129\3\2\2\2+\u012b\3\2\2\2-\u0135")
        buf.write("\3\2\2\2/\u013a\3\2\2\2\61\u0140\3\2\2\2\63\u0149\3\2")
        buf.write("\2\2\65\u014c\3\2\2\2\67\u0151\3\2\2\29\u0158\3\2\2\2")
        buf.write(";\u015e\3\2\2\2=\u0166\3\2\2\2?\u016d\3\2\2\2A\u0176\3")
        buf.write("\2\2\2C\u017a\3\2\2\2E\u0183\3\2\2\2G\u0186\3\2\2\2I\u0190")
        buf.write("\3\2\2\2K\u0197\3\2\2\2M\u019c\3\2\2\2O\u01a0\3\2\2\2")
        buf.write("Q\u01a6\3\2\2\2S\u01ab\3\2\2\2U\u01b1\3\2\2\2W\u01b7\3")
        buf.write("\2\2\2Y\u01b9\3\2\2\2[\u01bc\3\2\2\2]\u01be\3\2\2\2_\u01c1")
        buf.write("\3\2\2\2a\u01c3\3\2\2\2c\u01c6\3\2\2\2e\u01c8\3\2\2\2")
        buf.write("g\u01cb\3\2\2\2i\u01cd\3\2\2\2k\u01cf\3\2\2\2m\u01d2\3")
        buf.write("\2\2\2o\u01d5\3\2\2\2q\u01d8\3\2\2\2s\u01db\3\2\2\2u\u01dd")
        buf.write("\3\2\2\2w\u01df\3\2\2\2y\u01e2\3\2\2\2{\u01e5\3\2\2\2")
        buf.write("}\u01e9\3\2\2\2\177\u01ec\3\2\2\2\u0081\u01ef\3\2\2\2")
        buf.write("\u0083\u01f3\3\2\2\2\u0085\u01f7\3\2\2\2\u0087\u01f9\3")
        buf.write("\2\2\2\u0089\u01fb\3\2\2\2\u008b\u01fd\3\2\2\2\u008d\u01ff")
        buf.write("\3\2\2\2\u008f\u0201\3\2\2\2\u0091\u0203\3\2\2\2\u0093")
        buf.write("\u0205\3\2\2\2\u0095\u0207\3\2\2\2\u0097\u0209\3\2\2\2")
        buf.write("\u0099\u020b\3\2\2\2\u009b\u020d\3\2\2\2\u009d\u020f\3")
        buf.write("\2\2\2\u009f\u021c\3\2\2\2\u00a1\u022a\3\2\2\2\u00a3\u0237")
        buf.write("\3\2\2\2\u00a5\u0247\3\2\2\2\u00a7\u0256\3\2\2\2\u00a9")
        buf.write("\u0265\3\2\2\2\u00ab\u0273\3\2\2\2\u00ad\u0283\3\2\2\2")
        buf.write("\u00af\u0292\3\2\2\2\u00b1\u0298\3\2\2\2\u00b3\u02a2\3")
        buf.write("\2\2\2\u00b5\u02ae\3\2\2\2\u00b7\u02bb\3\2\2\2\u00b9\u00c0")
        buf.write("\5\5\3\2\u00ba\u00bf\5\5\3\2\u00bb\u00bf\5\t\5\2\u00bc")
        buf.write("\u00bf\5\7\4\2\u00bd\u00bf\7a\2\2\u00be\u00ba\3\2\2\2")
        buf.write("\u00be\u00bb\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bd\3")
        buf.write("\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4")
        buf.write("\t\2\2\2\u00c4\6\3\2\2\2\u00c5\u00c6\t\3\2\2\u00c6\b\3")
        buf.write("\2\2\2\u00c7\u00c8\t\4\2\2\u00c8\n\3\2\2\2\u00c9\u00cc")
        buf.write("\5\5\3\2\u00ca\u00cc\5\7\4\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\f\3\2\2\2\u00cd\u00d0\t\5\2\2\u00ce")
        buf.write("\u00d1\5[.\2\u00cf\u00d1\5W,\2\u00d0\u00ce\3\2\2\2\u00d0")
        buf.write("\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3\2\2\2")
        buf.write("\u00d2\u00d4\5\t\5\2\u00d3\u00d2\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\16")
        buf.write("\3\2\2\2\u00d7\u00db\t\6\2\2\u00d8\u00da\5\t\5\2\u00d9")
        buf.write("\u00d8\3\2\2\2\u00da\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\20\3\2\2\2\u00dd\u00db\3\2")
        buf.write("\2\2\u00de\u00e0\5\t\5\2\u00df\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\u00e8\3\2\2\2\u00e3\u00e5\5\17\b\2\u00e4\u00e6\5\r\7")
        buf.write("\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e9")
        buf.write("\3\2\2\2\u00e7\u00e9\5\r\7\2\u00e8\u00e3\3\2\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\22\3\2\2\2\u00ea\u00eb\7^\2\2\u00eb")
        buf.write("\u00ec\n\7\2\2\u00ec\24\3\2\2\2\u00ed\u00ee\7^\2\2\u00ee")
        buf.write("\u00ef\t\7\2\2\u00ef\26\3\2\2\2\u00f0\u00f1\7)\2\2\u00f1")
        buf.write("\u00f2\7$\2\2\u00f2\30\3\2\2\2\u00f3\u00f7\n\b\2\2\u00f4")
        buf.write("\u00f7\5\25\13\2\u00f5\u00f7\5\27\f\2\u00f6\u00f3\3\2")
        buf.write("\2\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\32")
        buf.write("\3\2\2\2\u00f8\u00f9\t\t\2\2\u00f9\34\3\2\2\2\u00fa\u00fb")
        buf.write("\t\n\2\2\u00fb\36\3\2\2\2\u00fc\u00fd\7\62\2\2\u00fd\u0101")
        buf.write("\7z\2\2\u00fe\u00ff\7\62\2\2\u00ff\u0101\7Z\2\2\u0100")
        buf.write("\u00fc\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0106\t\13\2\2\u0103\u0105\5\33\16\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107 \3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u0112\t\f\2\2\u010a\u010e\t\r\2\2\u010b\u010d\t\4\2\2")
        buf.write("\u010c\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010f\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0109\3\2\2\2\u0111\u010a\3\2\2\2\u0112")
        buf.write("\"\3\2\2\2\u0113\u0114\7\62\2\2\u0114\u0118\7q\2\2\u0115")
        buf.write("\u0116\7\62\2\2\u0116\u0118\7Q\2\2\u0117\u0113\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011d\t")
        buf.write("\16\2\2\u011a\u011c\5\35\17\2\u011b\u011a\3\2\2\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e$\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0124\5!\21")
        buf.write("\2\u0121\u0124\5\37\20\2\u0122\u0124\5#\22\2\u0123\u0120")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write("&\3\2\2\2\u0125\u0126\5\21\t\2\u0126(\3\2\2\2\u0127\u012a")
        buf.write("\5Q)\2\u0128\u012a\5S*\2\u0129\u0127\3\2\2\2\u0129\u0128")
        buf.write("\3\2\2\2\u012a*\3\2\2\2\u012b\u012f\5\u009bN\2\u012c\u012e")
        buf.write("\5\31\r\2\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3\2\2\2")
        buf.write("\u0131\u012f\3\2\2\2\u0132\u0133\5\u009bN\2\u0133\u0134")
        buf.write("\b\26\2\2\u0134,\3\2\2\2\u0135\u0136\7D\2\2\u0136\u0137")
        buf.write("\7q\2\2\u0137\u0138\7f\2\2\u0138\u0139\7{\2\2\u0139.\3")
        buf.write("\2\2\2\u013a\u013b\7D\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7g\2\2\u013d\u013e\7c\2\2\u013e\u013f\7m\2\2\u013f\60")
        buf.write("\3\2\2\2\u0140\u0141\7E\2\2\u0141\u0142\7q\2\2\u0142\u0143")
        buf.write("\7p\2\2\u0143\u0144\7v\2\2\u0144\u0145\7k\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\u0147\7w\2\2\u0147\u0148\7g\2\2\u0148\62")
        buf.write("\3\2\2\2\u0149\u014a\7F\2\2\u014a\u014b\7q\2\2\u014b\64")
        buf.write("\3\2\2\2\u014c\u014d\7G\2\2\u014d\u014e\7n\2\2\u014e\u014f")
        buf.write("\7u\2\2\u014f\u0150\7g\2\2\u0150\66\3\2\2\2\u0151\u0152")
        buf.write("\7G\2\2\u0152\u0153\7n\2\2\u0153\u0154\7u\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\u0156\7K\2\2\u0156\u0157\7h\2\2\u01578\3")
        buf.write("\2\2\2\u0158\u0159\7G\2\2\u0159\u015a\7p\2\2\u015a\u015b")
        buf.write("\7f\2\2\u015b\u015c\7K\2\2\u015c\u015d\7h\2\2\u015d:\3")
        buf.write("\2\2\2\u015e\u015f\7G\2\2\u015f\u0160\7p\2\2\u0160\u0161")
        buf.write("\7f\2\2\u0161\u0162\7D\2\2\u0162\u0163\7q\2\2\u0163\u0164")
        buf.write("\7f\2\2\u0164\u0165\7{\2\2\u0165<\3\2\2\2\u0166\u0167")
        buf.write("\7G\2\2\u0167\u0168\7p\2\2\u0168\u0169\7f\2\2\u0169\u016a")
        buf.write("\7H\2\2\u016a\u016b\7q\2\2\u016b\u016c\7t\2\2\u016c>\3")
        buf.write("\2\2\2\u016d\u016e\7G\2\2\u016e\u016f\7p\2\2\u016f\u0170")
        buf.write("\7f\2\2\u0170\u0171\7Y\2\2\u0171\u0172\7j\2\2\u0172\u0173")
        buf.write("\7k\2\2\u0173\u0174\7n\2\2\u0174\u0175\7g\2\2\u0175@\3")
        buf.write("\2\2\2\u0176\u0177\7H\2\2\u0177\u0178\7q\2\2\u0178\u0179")
        buf.write("\7t\2\2\u0179B\3\2\2\2\u017a\u017b\7H\2\2\u017b\u017c")
        buf.write("\7w\2\2\u017c\u017d\7p\2\2\u017d\u017e\7e\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017f\u0180\7k\2\2\u0180\u0181\7q\2\2\u0181\u0182")
        buf.write("\7p\2\2\u0182D\3\2\2\2\u0183\u0184\7K\2\2\u0184\u0185")
        buf.write("\7h\2\2\u0185F\3\2\2\2\u0186\u0187\7R\2\2\u0187\u0188")
        buf.write("\7c\2\2\u0188\u0189\7t\2\2\u0189\u018a\7c\2\2\u018a\u018b")
        buf.write("\7o\2\2\u018b\u018c\7g\2\2\u018c\u018d\7v\2\2\u018d\u018e")
        buf.write("\7g\2\2\u018e\u018f\7t\2\2\u018fH\3\2\2\2\u0190\u0191")
        buf.write("\7T\2\2\u0191\u0192\7g\2\2\u0192\u0193\7v\2\2\u0193\u0194")
        buf.write("\7w\2\2\u0194\u0195\7t\2\2\u0195\u0196\7p\2\2\u0196J\3")
        buf.write("\2\2\2\u0197\u0198\7V\2\2\u0198\u0199\7j\2\2\u0199\u019a")
        buf.write("\7g\2\2\u019a\u019b\7p\2\2\u019bL\3\2\2\2\u019c\u019d")
        buf.write("\7X\2\2\u019d\u019e\7c\2\2\u019e\u019f\7t\2\2\u019fN\3")
        buf.write("\2\2\2\u01a0\u01a1\7Y\2\2\u01a1\u01a2\7j\2\2\u01a2\u01a3")
        buf.write("\7k\2\2\u01a3\u01a4\7n\2\2\u01a4\u01a5\7g\2\2\u01a5P\3")
        buf.write("\2\2\2\u01a6\u01a7\7V\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9")
        buf.write("\7w\2\2\u01a9\u01aa\7g\2\2\u01aaR\3\2\2\2\u01ab\u01ac")
        buf.write("\7H\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae\7n\2\2\u01ae\u01af")
        buf.write("\7u\2\2\u01af\u01b0\7g\2\2\u01b0T\3\2\2\2\u01b1\u01b2")
        buf.write("\7G\2\2\u01b2\u01b3\7p\2\2\u01b3\u01b4\7f\2\2\u01b4\u01b5")
        buf.write("\7F\2\2\u01b5\u01b6\7q\2\2\u01b6V\3\2\2\2\u01b7\u01b8")
        buf.write("\7-\2\2\u01b8X\3\2\2\2\u01b9\u01ba\7-\2\2\u01ba\u01bb")
        buf.write("\7\60\2\2\u01bbZ\3\2\2\2\u01bc\u01bd\7/\2\2\u01bd\\\3")
        buf.write("\2\2\2\u01be\u01bf\7/\2\2\u01bf\u01c0\7\60\2\2\u01c0^")
        buf.write("\3\2\2\2\u01c1\u01c2\7,\2\2\u01c2`\3\2\2\2\u01c3\u01c4")
        buf.write("\7,\2\2\u01c4\u01c5\7\60\2\2\u01c5b\3\2\2\2\u01c6\u01c7")
        buf.write("\7^\2\2\u01c7d\3\2\2\2\u01c8\u01c9\7^\2\2\u01c9\u01ca")
        buf.write("\7\60\2\2\u01caf\3\2\2\2\u01cb\u01cc\7\'\2\2\u01cch\3")
        buf.write("\2\2\2\u01cd\u01ce\7#\2\2\u01cej\3\2\2\2\u01cf\u01d0\7")
        buf.write("(\2\2\u01d0\u01d1\7(\2\2\u01d1l\3\2\2\2\u01d2\u01d3\7")
        buf.write("~\2\2\u01d3\u01d4\7~\2\2\u01d4n\3\2\2\2\u01d5\u01d6\7")
        buf.write("?\2\2\u01d6\u01d7\7?\2\2\u01d7p\3\2\2\2\u01d8\u01d9\7")
        buf.write("#\2\2\u01d9\u01da\7?\2\2\u01dar\3\2\2\2\u01db\u01dc\7")
        buf.write(">\2\2\u01dct\3\2\2\2\u01dd\u01de\7@\2\2\u01dev\3\2\2\2")
        buf.write("\u01df\u01e0\7>\2\2\u01e0\u01e1\7?\2\2\u01e1x\3\2\2\2")
        buf.write("\u01e2\u01e3\7@\2\2\u01e3\u01e4\7?\2\2\u01e4z\3\2\2\2")
        buf.write("\u01e5\u01e6\7?\2\2\u01e6\u01e7\7\61\2\2\u01e7\u01e8\7")
        buf.write("?\2\2\u01e8|\3\2\2\2\u01e9\u01ea\7>\2\2\u01ea\u01eb\7")
        buf.write("\60\2\2\u01eb~\3\2\2\2\u01ec\u01ed\7@\2\2\u01ed\u01ee")
        buf.write("\7\60\2\2\u01ee\u0080\3\2\2\2\u01ef\u01f0\7>\2\2\u01f0")
        buf.write("\u01f1\7?\2\2\u01f1\u01f2\7\60\2\2\u01f2\u0082\3\2\2\2")
        buf.write("\u01f3\u01f4\7@\2\2\u01f4\u01f5\7?\2\2\u01f5\u01f6\7\60")
        buf.write("\2\2\u01f6\u0084\3\2\2\2\u01f7\u01f8\7*\2\2\u01f8\u0086")
        buf.write("\3\2\2\2\u01f9\u01fa\7+\2\2\u01fa\u0088\3\2\2\2\u01fb")
        buf.write("\u01fc\7]\2\2\u01fc\u008a\3\2\2\2\u01fd\u01fe\7_\2\2\u01fe")
        buf.write("\u008c\3\2\2\2\u01ff\u0200\7}\2\2\u0200\u008e\3\2\2\2")
        buf.write("\u0201\u0202\7\177\2\2\u0202\u0090\3\2\2\2\u0203\u0204")
        buf.write("\7<\2\2\u0204\u0092\3\2\2\2\u0205\u0206\7\60\2\2\u0206")
        buf.write("\u0094\3\2\2\2\u0207\u0208\7=\2\2\u0208\u0096\3\2\2\2")
        buf.write("\u0209\u020a\7.\2\2\u020a\u0098\3\2\2\2\u020b\u020c\7")
        buf.write("?\2\2\u020c\u009a\3\2\2\2\u020d\u020e\7$\2\2\u020e\u009c")
        buf.write("\3\2\2\2\u020f\u0210\7k\2\2\u0210\u0211\7p\2\2\u0211\u0212")
        buf.write("\7v\2\2\u0212\u0213\7a\2\2\u0213\u0214\7q\2\2\u0214\u0215")
        buf.write("\7h\2\2\u0215\u0216\7a\2\2\u0216\u0217\7h\2\2\u0217\u0218")
        buf.write("\7n\2\2\u0218\u0219\7q\2\2\u0219\u021a\7c\2\2\u021a\u021b")
        buf.write("\7v\2\2\u021b\u009e\3\2\2\2\u021c\u021d\7k\2\2\u021d\u021e")
        buf.write("\7p\2\2\u021e\u021f\7v\2\2\u021f\u0220\7a\2\2\u0220\u0221")
        buf.write("\7q\2\2\u0221\u0222\7h\2\2\u0222\u0223\7a\2\2\u0223\u0224")
        buf.write("\7u\2\2\u0224\u0225\7v\2\2\u0225\u0226\7t\2\2\u0226\u0227")
        buf.write("\7k\2\2\u0227\u0228\7p\2\2\u0228\u0229\7i\2\2\u0229\u00a0")
        buf.write("\3\2\2\2\u022a\u022b\7h\2\2\u022b\u022c\7n\2\2\u022c\u022d")
        buf.write("\7q\2\2\u022d\u022e\7c\2\2\u022e\u022f\7v\2\2\u022f\u0230")
        buf.write("\7a\2\2\u0230\u0231\7v\2\2\u0231\u0232\7q\2\2\u0232\u0233")
        buf.write("\7a\2\2\u0233\u0234\7k\2\2\u0234\u0235\7p\2\2\u0235\u0236")
        buf.write("\7v\2\2\u0236\u00a2\3\2\2\2\u0237\u0238\7h\2\2\u0238\u0239")
        buf.write("\7n\2\2\u0239\u023a\7q\2\2\u023a\u023b\7c\2\2\u023b\u023c")
        buf.write("\7v\2\2\u023c\u023d\7a\2\2\u023d\u023e\7q\2\2\u023e\u023f")
        buf.write("\7h\2\2\u023f\u0240\7a\2\2\u0240\u0241\7u\2\2\u0241\u0242")
        buf.write("\7v\2\2\u0242\u0243\7t\2\2\u0243\u0244\7k\2\2\u0244\u0245")
        buf.write("\7p\2\2\u0245\u0246\7i\2\2\u0246\u00a4\3\2\2\2\u0247\u0248")
        buf.write("\7d\2\2\u0248\u0249\7q\2\2\u0249\u024a\7q\2\2\u024a\u024b")
        buf.write("\7n\2\2\u024b\u024c\7a\2\2\u024c\u024d\7q\2\2\u024d\u024e")
        buf.write("\7h\2\2\u024e\u024f\7a\2\2\u024f\u0250\7u\2\2\u0250\u0251")
        buf.write("\7v\2\2\u0251\u0252\7t\2\2\u0252\u0253\7k\2\2\u0253\u0254")
        buf.write("\7p\2\2\u0254\u0255\7i\2\2\u0255\u00a6\3\2\2\2\u0256\u0257")
        buf.write("\7u\2\2\u0257\u0258\7v\2\2\u0258\u0259\7t\2\2\u0259\u025a")
        buf.write("\7k\2\2\u025a\u025b\7p\2\2\u025b\u025c\7i\2\2\u025c\u025d")
        buf.write("\7a\2\2\u025d\u025e\7q\2\2\u025e\u025f\7h\2\2\u025f\u0260")
        buf.write("\7a\2\2\u0260\u0261\7d\2\2\u0261\u0262\7q\2\2\u0262\u0263")
        buf.write("\7q\2\2\u0263\u0264\7n\2\2\u0264\u00a8\3\2\2\2\u0265\u0266")
        buf.write("\7u\2\2\u0266\u0267\7v\2\2\u0267\u0268\7t\2\2\u0268\u0269")
        buf.write("\7k\2\2\u0269\u026a\7p\2\2\u026a\u026b\7i\2\2\u026b\u026c")
        buf.write("\7a\2\2\u026c\u026d\7q\2\2\u026d\u026e\7h\2\2\u026e\u026f")
        buf.write("\7a\2\2\u026f\u0270\7k\2\2\u0270\u0271\7p\2\2\u0271\u0272")
        buf.write("\7v\2\2\u0272\u00aa\3\2\2\2\u0273\u0274\7u\2\2\u0274\u0275")
        buf.write("\7v\2\2\u0275\u0276\7t\2\2\u0276\u0277\7k\2\2\u0277\u0278")
        buf.write("\7p\2\2\u0278\u0279\7i\2\2\u0279\u027a\7a\2\2\u027a\u027b")
        buf.write("\7q\2\2\u027b\u027c\7h\2\2\u027c\u027d\7a\2\2\u027d\u027e")
        buf.write("\7h\2\2\u027e\u027f\7n\2\2\u027f\u0280\7q\2\2\u0280\u0281")
        buf.write("\7c\2\2\u0281\u0282\7v\2\2\u0282\u00ac\3\2\2\2\u0283\u0284")
        buf.write("\7,\2\2\u0284\u0285\7,\2\2\u0285\u0289\3\2\2\2\u0286\u0288")
        buf.write("\13\2\2\2\u0287\u0286\3\2\2\2\u0288\u028b\3\2\2\2\u0289")
        buf.write("\u028a\3\2\2\2\u0289\u0287\3\2\2\2\u028a\u028c\3\2\2\2")
        buf.write("\u028b\u0289\3\2\2\2\u028c\u028d\7,\2\2\u028d\u028e\7")
        buf.write(",\2\2\u028e\u028f\3\2\2\2\u028f\u0290\bW\3\2\u0290\u00ae")
        buf.write("\3\2\2\2\u0291\u0293\t\17\2\2\u0292\u0291\3\2\2\2\u0293")
        buf.write("\u0294\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2\2\2")
        buf.write("\u0295\u0296\3\2\2\2\u0296\u0297\bX\3\2\u0297\u00b0\3")
        buf.write("\2\2\2\u0298\u029c\7$\2\2\u0299\u029b\5\31\r\2\u029a\u0299")
        buf.write("\3\2\2\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2\u029c")
        buf.write("\u029d\3\2\2\2\u029d\u029f\3\2\2\2\u029e\u029c\3\2\2\2")
        buf.write("\u029f\u02a0\5\23\n\2\u02a0\u02a1\bY\4\2\u02a1\u00b2\3")
        buf.write("\2\2\2\u02a2\u02a6\7$\2\2\u02a3\u02a5\5\31\r\2\u02a4\u02a3")
        buf.write("\3\2\2\2\u02a5\u02a8\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a6")
        buf.write("\u02a7\3\2\2\2\u02a7\u02aa\3\2\2\2\u02a8\u02a6\3\2\2\2")
        buf.write("\u02a9\u02ab\t\20\2\2\u02aa\u02a9\3\2\2\2\u02ab\u02ac")
        buf.write("\3\2\2\2\u02ac\u02ad\bZ\5\2\u02ad\u00b4\3\2\2\2\u02ae")
        buf.write("\u02af\7,\2\2\u02af\u02b0\7,\2\2\u02b0\u02b6\3\2\2\2\u02b1")
        buf.write("\u02b2\7,\2\2\u02b2\u02b5\n\21\2\2\u02b3\u02b5\n\21\2")
        buf.write("\2\u02b4\u02b1\3\2\2\2\u02b4\u02b3\3\2\2\2\u02b5\u02b8")
        buf.write("\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b6\u02b4\3\2\2\2\u02b7")
        buf.write("\u02b9\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b9\u02ba\7\2\2\3")
        buf.write("\u02ba\u00b6\3\2\2\2\u02bb\u02bc\13\2\2\2\u02bc\u00b8")
        buf.write("\3\2\2\2\35\2\u00be\u00c0\u00cb\u00d0\u00d5\u00db\u00e1")
        buf.write("\u00e5\u00e8\u00f6\u0100\u0106\u010e\u0111\u0117\u011d")
        buf.write("\u0123\u0129\u012f\u0289\u0294\u029c\u02a6\u02aa\u02b4")
        buf.write("\u02b6\6\3\26\2\b\2\2\3Y\3\3Z\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INT_LIT = 2
    FLOAT_LIT = 3
    BOOL_LIT = 4
    STRING_LIT = 5
    BODY = 6
    BREAK = 7
    CONTINUE = 8
    DO = 9
    ELSE = 10
    ELSEIF = 11
    ENDIF = 12
    ENDBODY = 13
    ENDFOR = 14
    ENDWHILE = 15
    FOR = 16
    FUNCTION = 17
    IF = 18
    PARAMETER = 19
    RETURN = 20
    THEN = 21
    VAR = 22
    WHILE = 23
    TRUE = 24
    FALSE = 25
    ENDDO = 26
    PLUS_INT = 27
    PLUS_FLOAT = 28
    MINUS_INT = 29
    MINUS_FLOAT = 30
    STAR_INT = 31
    STAR_FLOAT = 32
    DIV_INT = 33
    DIV_FLOAT = 34
    MOD = 35
    NOT = 36
    AND = 37
    OR = 38
    EQUAL = 39
    NOT_EQUAL_INT = 40
    LESS_INT = 41
    GREATER_INT = 42
    LESS_OR_EQUAL_INT = 43
    GREATER_OR_EQUAL_INT = 44
    NOT_EQUAL_FLOAT = 45
    LESS_FLOAT = 46
    GREATER_FLOAT = 47
    LESS_OR_EQUAL_FLOAT = 48
    GREATER_OR_EQUAL_FLOAT = 49
    LEFT_PAREN = 50
    RIGHT_PAREN = 51
    LEFT_BRACKET = 52
    RIGHT_BRACKET = 53
    LEFT_BRACE = 54
    RIGHT_BRACE = 55
    COLON = 56
    DOT = 57
    SEMI = 58
    COMMA = 59
    ASSIGN = 60
    DOUBLE_QUOTE = 61
    INT_OF_FLOAT = 62
    INT_OF_STRING = 63
    FLOAT_TO_INT = 64
    FLOAT_OF_STRING = 65
    BOOL_OF_STRING = 66
    STRING_OF_BOOL = 67
    STRING_OF_INT = 68
    STRING_OF_FLOAT = 69
    COMMENT = 70
    WS = 71
    ILLEGAL_ESCAPE = 72
    UNCLOSE_STRING = 73
    UNTERMINATED_COMMENT = 74
    ERROR_CHAR = 75

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
            "ID", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "BODY", 
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

    ruleNames = [ "ID", "LOWERCASE_LETTER", "UPPERCASE_LETTER", "DIGIT", 
                  "LETTER", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
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
            actions[20] = self.STRING_LIT_action 
            actions[87] = self.ILLEGAL_ESCAPE_action 
            actions[88] = self.UNCLOSE_STRING_action 
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
                
     


