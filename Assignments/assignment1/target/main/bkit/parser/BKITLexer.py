# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2Q")
        buf.write("\u0307\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u00d5\n\3\f\3\16")
        buf.write("\3\u00d8\13\3\3\3\3\3\5\3\u00dc\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u00e3\n\4\f\4\16\4\u00e6\13\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5\u00ef\n\5\f\5\16\5\u00f2\13\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6\u00fb\n\6\f\6\16\6\u00fe\13\6\3")
        buf.write("\6\3\6\3\7\3\7\5\7\u0104\n\7\3\b\3\b\5\b\u0108\n\b\3\t")
        buf.write("\3\t\5\t\u010c\n\t\3\n\3\n\3\n\7\n\u0111\n\n\f\n\16\n")
        buf.write("\u0114\13\n\3\13\3\13\7\13\u0118\n\13\f\13\16\13\u011b")
        buf.write("\13\13\3\13\3\13\3\f\3\f\7\f\u0121\n\f\f\f\16\f\u0124")
        buf.write("\13\f\3\f\5\f\u0127\n\f\3\f\3\f\3\r\3\r\3\r\3\r\7\r\u012f")
        buf.write("\n\r\f\r\16\r\u0132\13\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\7\16\u013f\n\16\f\16\16\16\u0142")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\20\6\20\u0149\n\20\r\20\16")
        buf.write("\20\u014a\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24")
        buf.write("\3\24\5\24\u0157\n\24\3\25\3\25\5\25\u015b\n\25\3\25\6")
        buf.write("\25\u015e\n\25\r\25\16\25\u015f\3\26\3\26\7\26\u0164\n")
        buf.write("\26\f\26\16\26\u0167\13\26\3\27\6\27\u016a\n\27\r\27\16")
        buf.write("\27\u016b\3\27\3\27\5\27\u0170\n\27\3\27\5\27\u0173\n")
        buf.write("\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\5\33\u0181\n\33\3\34\3\34\3\35\3\35\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u018b\n\36\3\36\6\36\u018e\n\36\r\36")
        buf.write("\16\36\u018f\3\37\6\37\u0193\n\37\r\37\16\37\u0194\3 ")
        buf.write("\3 \3 \3 \5 \u019b\n \3 \6 \u019e\n \r \16 \u019f\3!\3")
        buf.write("!\3!\5!\u01a5\n!\3\"\3\"\3#\3#\5#\u01ab\n#\3$\3$\7$\u01af")
        buf.write("\n$\f$\16$\u01b2\13$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\38\38\38\38\38\38\39\39\39\39\39\39\3")
        buf.write("9\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3")
        buf.write("A\3A\3A\3B\3B\3C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3")
        buf.write("G\3H\3H\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3L\3L\3M\3M\3M\3")
        buf.write("N\3N\3N\3O\3O\3O\3O\3P\3P\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3")
        buf.write("T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3")
        buf.write("\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3]\3]\3]\3")
        buf.write("]\3]\3]\3]\3]\3]\3]\3]\3]\3]\3]\3^\3^\3^\3^\3^\3^\3^\3")
        buf.write("^\3^\3^\3^\3^\3^\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3")
        buf.write("_\3_\3_\3_\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\3")
        buf.write("`\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3a\3b\3b\3")
        buf.write("b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3b\3c\3c\3c\3c\3c\3c\3")
        buf.write("c\3c\3c\3c\3c\3c\3c\3c\3c\3c\4\u0130\u0140\2d\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\2\17\2\21\2\23\b\25\t\27\n\31\13\33\f")
        buf.write("\35\r\37\16!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67")
        buf.write("\29\2;\2=\2?\2A\17C\20E\21G\22I\23K\24M\25O\26Q\27S\30")
        buf.write("U\31W\32Y\33[\34]\35_\36a\37c e!g\"i#k$m%o&q\'s(u)w*y")
        buf.write("+{,}-\177.\u0081/\u0083\60\u0085\61\u0087\62\u0089\63")
        buf.write("\u008b\64\u008d\65\u008f\66\u0091\67\u00938\u00959\u0097")
        buf.write(":\u0099;\u009b<\u009d=\u009f>\u00a1?\u00a3@\u00a5A\u00a7")
        buf.write("B\u00a9C\u00abD\u00adE\u00afF\u00b1G\u00b3H\u00b5I\u00b7")
        buf.write("J\u00b9K\u00bbL\u00bdM\u00bfN\u00c1O\u00c3P\u00c5Q\3\2")
        buf.write("\17\4\3\n\f\16\17\3\2,,\4\2\60\60AA\5\2\13\f\16\17\"\"")
        buf.write("\3\2c|\3\2C\\\3\2\62;\4\2GGgg\3\2\60\60\t\2))^^ddhhpp")
        buf.write("ttvv\7\2\n\f\16\17$$))^^\5\2\62;CHch\3\2\629\2\u0317\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\3\u00c7\3\2\2\2\5\u00db")
        buf.write("\3\2\2\2\7\u00dd\3\2\2\2\t\u00e9\3\2\2\2\13\u00f5\3\2")
        buf.write("\2\2\r\u0103\3\2\2\2\17\u0107\3\2\2\2\21\u010b\3\2\2\2")
        buf.write("\23\u010d\3\2\2\2\25\u0115\3\2\2\2\27\u011e\3\2\2\2\31")
        buf.write("\u012a\3\2\2\2\33\u0138\3\2\2\2\35\u0145\3\2\2\2\37\u0148")
        buf.write("\3\2\2\2!\u014e\3\2\2\2#\u0150\3\2\2\2%\u0152\3\2\2\2")
        buf.write("\'\u0156\3\2\2\2)\u0158\3\2\2\2+\u0161\3\2\2\2-\u0169")
        buf.write("\3\2\2\2/\u0174\3\2\2\2\61\u0177\3\2\2\2\63\u017a\3\2")
        buf.write("\2\2\65\u0180\3\2\2\2\67\u0182\3\2\2\29\u0184\3\2\2\2")
        buf.write(";\u018a\3\2\2\2=\u0192\3\2\2\2?\u019a\3\2\2\2A\u01a4\3")
        buf.write("\2\2\2C\u01a6\3\2\2\2E\u01aa\3\2\2\2G\u01ac\3\2\2\2I\u01b6")
        buf.write("\3\2\2\2K\u01bb\3\2\2\2M\u01c1\3\2\2\2O\u01ca\3\2\2\2")
        buf.write("Q\u01cd\3\2\2\2S\u01d2\3\2\2\2U\u01d9\3\2\2\2W\u01e0\3")
        buf.write("\2\2\2Y\u01e9\3\2\2\2[\u01f1\3\2\2\2]\u01fb\3\2\2\2_\u01ff")
        buf.write("\3\2\2\2a\u0208\3\2\2\2c\u020b\3\2\2\2e\u0215\3\2\2\2")
        buf.write("g\u021c\3\2\2\2i\u0221\3\2\2\2k\u0225\3\2\2\2m\u022b\3")
        buf.write("\2\2\2o\u0230\3\2\2\2q\u0236\3\2\2\2s\u023d\3\2\2\2u\u023f")
        buf.write("\3\2\2\2w\u0242\3\2\2\2y\u0244\3\2\2\2{\u0247\3\2\2\2")
        buf.write("}\u0249\3\2\2\2\177\u024c\3\2\2\2\u0081\u024e\3\2\2\2")
        buf.write("\u0083\u0251\3\2\2\2\u0085\u0253\3\2\2\2\u0087\u0255\3")
        buf.write("\2\2\2\u0089\u0258\3\2\2\2\u008b\u025b\3\2\2\2\u008d\u025e")
        buf.write("\3\2\2\2\u008f\u0261\3\2\2\2\u0091\u0263\3\2\2\2\u0093")
        buf.write("\u0265\3\2\2\2\u0095\u0268\3\2\2\2\u0097\u026b\3\2\2\2")
        buf.write("\u0099\u026f\3\2\2\2\u009b\u0272\3\2\2\2\u009d\u0275\3")
        buf.write("\2\2\2\u009f\u0279\3\2\2\2\u00a1\u027d\3\2\2\2\u00a3\u027f")
        buf.write("\3\2\2\2\u00a5\u0281\3\2\2\2\u00a7\u0283\3\2\2\2\u00a9")
        buf.write("\u0285\3\2\2\2\u00ab\u0287\3\2\2\2\u00ad\u0289\3\2\2\2")
        buf.write("\u00af\u028b\3\2\2\2\u00b1\u028d\3\2\2\2\u00b3\u028f\3")
        buf.write("\2\2\2\u00b5\u0291\3\2\2\2\u00b7\u0293\3\2\2\2\u00b9\u02a0")
        buf.write("\3\2\2\2\u00bb\u02ae\3\2\2\2\u00bd\u02bb\3\2\2\2\u00bf")
        buf.write("\u02cb\3\2\2\2\u00c1\u02da\3\2\2\2\u00c3\u02e9\3\2\2\2")
        buf.write("\u00c5\u02f7\3\2\2\2\u00c7\u00c8\7o\2\2\u00c8\u00c9\7")
        buf.write("c\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb\7p\2\2\u00cb\4\3")
        buf.write("\2\2\2\u00cc\u00dc\5\7\4\2\u00cd\u00dc\5\t\5\2\u00ce\u00dc")
        buf.write("\5\13\6\2\u00cf\u00d0\5\u00a9U\2\u00d0\u00d6\5\5\3\2\u00d1")
        buf.write("\u00d2\5\u00b3Z\2\u00d2\u00d3\5\5\3\2\u00d3\u00d5\3\2")
        buf.write("\2\2\u00d4\u00d1\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00da\5\u00abV\2\u00da\u00dc\3\2")
        buf.write("\2\2\u00db\u00cc\3\2\2\2\u00db\u00cd\3\2\2\2\u00db\u00ce")
        buf.write("\3\2\2\2\u00db\u00cf\3\2\2\2\u00dc\6\3\2\2\2\u00dd\u00de")
        buf.write("\5\u00a9U\2\u00de\u00e4\5\r\7\2\u00df\u00e0\5\u00b3Z\2")
        buf.write("\u00e0\u00e1\5\r\7\2\u00e1\u00e3\3\2\2\2\u00e2\u00df\3")
        buf.write("\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write("\u00e8\5\u00abV\2\u00e8\b\3\2\2\2\u00e9\u00ea\5\u00a9")
        buf.write("U\2\u00ea\u00f0\5\17\b\2\u00eb\u00ec\5\u00b3Z\2\u00ec")
        buf.write("\u00ed\5\17\b\2\u00ed\u00ef\3\2\2\2\u00ee\u00eb\3\2\2")
        buf.write("\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3")
        buf.write("\u00f4\5\u00abV\2\u00f4\n\3\2\2\2\u00f5\u00f6\5\u00a9")
        buf.write("U\2\u00f6\u00fc\5\21\t\2\u00f7\u00f8\5\u00b3Z\2\u00f8")
        buf.write("\u00f9\5\21\t\2\u00f9\u00fb\3\2\2\2\u00fa\u00f7\3\2\2")
        buf.write("\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write("\u0100\5\u00abV\2\u0100\f\3\2\2\2\u0101\u0104\5A!\2\u0102")
        buf.write("\u0104\5\23\n\2\u0103\u0101\3\2\2\2\u0103\u0102\3\2\2")
        buf.write("\2\u0104\16\3\2\2\2\u0105\u0108\5C\"\2\u0106\u0108\5\23")
        buf.write("\n\2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108\20")
        buf.write("\3\2\2\2\u0109\u010c\5G$\2\u010a\u010c\5\23\n\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010a\3\2\2\2\u010c\22\3\2\2\2\u010d")
        buf.write("\u0112\5!\21\2\u010e\u0111\5!\21\2\u010f\u0111\5%\23\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3")
        buf.write("\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113\24")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0119\7$\2\2\u0116")
        buf.write("\u0118\5\65\33\2\u0117\u0116\3\2\2\2\u0118\u011b\3\2\2")
        buf.write("\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011c")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\5/\30\2\u011d")
        buf.write("\26\3\2\2\2\u011e\u0122\7$\2\2\u011f\u0121\5\65\33\2\u0120")
        buf.write("\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3")
        buf.write("\2\2\2\u0125\u0127\t\2\2\2\u0126\u0125\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u0129\b\f\2\2\u0129\30\3\2\2\2\u012a\u012b")
        buf.write("\7,\2\2\u012b\u012c\7,\2\2\u012c\u0130\3\2\2\2\u012d\u012f")
        buf.write("\13\2\2\2\u012e\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0133\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0133\u0134\7,\2\2\u0134\u0135\7")
        buf.write(",\2\2\u0135\u0136\3\2\2\2\u0136\u0137\b\r\3\2\u0137\32")
        buf.write("\3\2\2\2\u0138\u0139\7,\2\2\u0139\u013a\7,\2\2\u013a\u0140")
        buf.write("\3\2\2\2\u013b\u013c\7,\2\2\u013c\u013f\n\3\2\2\u013d")
        buf.write("\u013f\n\3\2\2\u013e\u013b\3\2\2\2\u013e\u013d\3\2\2\2")
        buf.write("\u013f\u0142\3\2\2\2\u0140\u0141\3\2\2\2\u0140\u013e\3")
        buf.write("\2\2\2\u0141\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144")
        buf.write("\7\2\2\3\u0144\34\3\2\2\2\u0145\u0146\t\4\2\2\u0146\36")
        buf.write("\3\2\2\2\u0147\u0149\t\5\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u014c\3\2\2\2\u014c\u014d\b\20\3\2\u014d \3\2\2")
        buf.write("\2\u014e\u014f\t\6\2\2\u014f\"\3\2\2\2\u0150\u0151\t\7")
        buf.write("\2\2\u0151$\3\2\2\2\u0152\u0153\t\b\2\2\u0153&\3\2\2\2")
        buf.write("\u0154\u0157\5!\21\2\u0155\u0157\5#\22\2\u0156\u0154\3")
        buf.write("\2\2\2\u0156\u0155\3\2\2\2\u0157(\3\2\2\2\u0158\u015a")
        buf.write("\t\t\2\2\u0159\u015b\5w<\2\u015a\u0159\3\2\2\2\u015a\u015b")
        buf.write("\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015e\5%\23\2\u015d")
        buf.write("\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u0160\3\2\2\2\u0160*\3\2\2\2\u0161\u0165\t\n\2")
        buf.write("\2\u0162\u0164\5%\23\2\u0163\u0162\3\2\2\2\u0164\u0167")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write(",\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a\5%\23\2\u0169")
        buf.write("\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0169\3\2\2\2")
        buf.write("\u016b\u016c\3\2\2\2\u016c\u0172\3\2\2\2\u016d\u016f\5")
        buf.write("+\26\2\u016e\u0170\5)\25\2\u016f\u016e\3\2\2\2\u016f\u0170")
        buf.write("\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u0173\5)\25\2\u0172")
        buf.write("\u016d\3\2\2\2\u0172\u0171\3\2\2\2\u0173.\3\2\2\2\u0174")
        buf.write("\u0175\7^\2\2\u0175\u0176\n\13\2\2\u0176\60\3\2\2\2\u0177")
        buf.write("\u0178\7^\2\2\u0178\u0179\t\13\2\2\u0179\62\3\2\2\2\u017a")
        buf.write("\u017b\7)\2\2\u017b\u017c\7$\2\2\u017c\64\3\2\2\2\u017d")
        buf.write("\u0181\n\f\2\2\u017e\u0181\5\61\31\2\u017f\u0181\5\63")
        buf.write("\32\2\u0180\u017d\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u017f")
        buf.write("\3\2\2\2\u0181\66\3\2\2\2\u0182\u0183\t\r\2\2\u01838\3")
        buf.write("\2\2\2\u0184\u0185\t\16\2\2\u0185:\3\2\2\2\u0186\u0187")
        buf.write("\7\62\2\2\u0187\u018b\7z\2\2\u0188\u0189\7\62\2\2\u0189")
        buf.write("\u018b\7Z\2\2\u018a\u0186\3\2\2\2\u018a\u0188\3\2\2\2")
        buf.write("\u018b\u018d\3\2\2\2\u018c\u018e\5\67\34\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190<\3\2\2\2\u0191\u0193\5%\23\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195>\3\2\2\2\u0196\u0197\7\62\2")
        buf.write("\2\u0197\u019b\7q\2\2\u0198\u0199\7\62\2\2\u0199\u019b")
        buf.write("\7Q\2\2\u019a\u0196\3\2\2\2\u019a\u0198\3\2\2\2\u019b")
        buf.write("\u019d\3\2\2\2\u019c\u019e\59\35\2\u019d\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0@\3\2\2\2\u01a1\u01a5\5=\37\2\u01a2\u01a5")
        buf.write("\5;\36\2\u01a3\u01a5\5? \2\u01a4\u01a1\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5B\3\2\2\2\u01a6\u01a7")
        buf.write("\5-\27\2\u01a7D\3\2\2\2\u01a8\u01ab\5m\67\2\u01a9\u01ab")
        buf.write("\5o8\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abF")
        buf.write("\3\2\2\2\u01ac\u01b0\7$\2\2\u01ad\u01af\5\65\33\2\u01ae")
        buf.write("\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3")
        buf.write("\2\2\2\u01b3\u01b4\7$\2\2\u01b4\u01b5\b$\4\2\u01b5H\3")
        buf.write("\2\2\2\u01b6\u01b7\7D\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9")
        buf.write("\7f\2\2\u01b9\u01ba\7{\2\2\u01baJ\3\2\2\2\u01bb\u01bc")
        buf.write("\7D\2\2\u01bc\u01bd\7t\2\2\u01bd\u01be\7g\2\2\u01be\u01bf")
        buf.write("\7c\2\2\u01bf\u01c0\7m\2\2\u01c0L\3\2\2\2\u01c1\u01c2")
        buf.write("\7E\2\2\u01c2\u01c3\7q\2\2\u01c3\u01c4\7p\2\2\u01c4\u01c5")
        buf.write("\7v\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7\7p\2\2\u01c7\u01c8")
        buf.write("\7w\2\2\u01c8\u01c9\7g\2\2\u01c9N\3\2\2\2\u01ca\u01cb")
        buf.write("\7F\2\2\u01cb\u01cc\7q\2\2\u01ccP\3\2\2\2\u01cd\u01ce")
        buf.write("\7G\2\2\u01ce\u01cf\7n\2\2\u01cf\u01d0\7u\2\2\u01d0\u01d1")
        buf.write("\7g\2\2\u01d1R\3\2\2\2\u01d2\u01d3\7G\2\2\u01d3\u01d4")
        buf.write("\7n\2\2\u01d4\u01d5\7u\2\2\u01d5\u01d6\7g\2\2\u01d6\u01d7")
        buf.write("\7K\2\2\u01d7\u01d8\7h\2\2\u01d8T\3\2\2\2\u01d9\u01da")
        buf.write("\7G\2\2\u01da\u01db\7p\2\2\u01db\u01dc\7f\2\2\u01dc\u01dd")
        buf.write("\7K\2\2\u01dd\u01de\7h\2\2\u01de\u01df\7\60\2\2\u01df")
        buf.write("V\3\2\2\2\u01e0\u01e1\7G\2\2\u01e1\u01e2\7p\2\2\u01e2")
        buf.write("\u01e3\7f\2\2\u01e3\u01e4\7D\2\2\u01e4\u01e5\7q\2\2\u01e5")
        buf.write("\u01e6\7f\2\2\u01e6\u01e7\7{\2\2\u01e7\u01e8\7\60\2\2")
        buf.write("\u01e8X\3\2\2\2\u01e9\u01ea\7G\2\2\u01ea\u01eb\7p\2\2")
        buf.write("\u01eb\u01ec\7f\2\2\u01ec\u01ed\7H\2\2\u01ed\u01ee\7q")
        buf.write("\2\2\u01ee\u01ef\7t\2\2\u01ef\u01f0\7\60\2\2\u01f0Z\3")
        buf.write("\2\2\2\u01f1\u01f2\7G\2\2\u01f2\u01f3\7p\2\2\u01f3\u01f4")
        buf.write("\7f\2\2\u01f4\u01f5\7Y\2\2\u01f5\u01f6\7j\2\2\u01f6\u01f7")
        buf.write("\7k\2\2\u01f7\u01f8\7n\2\2\u01f8\u01f9\7g\2\2\u01f9\u01fa")
        buf.write("\7\60\2\2\u01fa\\\3\2\2\2\u01fb\u01fc\7H\2\2\u01fc\u01fd")
        buf.write("\7q\2\2\u01fd\u01fe\7t\2\2\u01fe^\3\2\2\2\u01ff\u0200")
        buf.write("\7H\2\2\u0200\u0201\7w\2\2\u0201\u0202\7p\2\2\u0202\u0203")
        buf.write("\7e\2\2\u0203\u0204\7v\2\2\u0204\u0205\7k\2\2\u0205\u0206")
        buf.write("\7q\2\2\u0206\u0207\7p\2\2\u0207`\3\2\2\2\u0208\u0209")
        buf.write("\7K\2\2\u0209\u020a\7h\2\2\u020ab\3\2\2\2\u020b\u020c")
        buf.write("\7R\2\2\u020c\u020d\7c\2\2\u020d\u020e\7t\2\2\u020e\u020f")
        buf.write("\7c\2\2\u020f\u0210\7o\2\2\u0210\u0211\7g\2\2\u0211\u0212")
        buf.write("\7v\2\2\u0212\u0213\7g\2\2\u0213\u0214\7t\2\2\u0214d\3")
        buf.write("\2\2\2\u0215\u0216\7T\2\2\u0216\u0217\7g\2\2\u0217\u0218")
        buf.write("\7v\2\2\u0218\u0219\7w\2\2\u0219\u021a\7t\2\2\u021a\u021b")
        buf.write("\7p\2\2\u021bf\3\2\2\2\u021c\u021d\7V\2\2\u021d\u021e")
        buf.write("\7j\2\2\u021e\u021f\7g\2\2\u021f\u0220\7p\2\2\u0220h\3")
        buf.write("\2\2\2\u0221\u0222\7X\2\2\u0222\u0223\7c\2\2\u0223\u0224")
        buf.write("\7t\2\2\u0224j\3\2\2\2\u0225\u0226\7Y\2\2\u0226\u0227")
        buf.write("\7j\2\2\u0227\u0228\7k\2\2\u0228\u0229\7n\2\2\u0229\u022a")
        buf.write("\7g\2\2\u022al\3\2\2\2\u022b\u022c\7V\2\2\u022c\u022d")
        buf.write("\7t\2\2\u022d\u022e\7w\2\2\u022e\u022f\7g\2\2\u022fn\3")
        buf.write("\2\2\2\u0230\u0231\7H\2\2\u0231\u0232\7c\2\2\u0232\u0233")
        buf.write("\7n\2\2\u0233\u0234\7u\2\2\u0234\u0235\7g\2\2\u0235p\3")
        buf.write("\2\2\2\u0236\u0237\7G\2\2\u0237\u0238\7p\2\2\u0238\u0239")
        buf.write("\7f\2\2\u0239\u023a\7F\2\2\u023a\u023b\7q\2\2\u023b\u023c")
        buf.write("\7\60\2\2\u023cr\3\2\2\2\u023d\u023e\7-\2\2\u023et\3\2")
        buf.write("\2\2\u023f\u0240\7-\2\2\u0240\u0241\7\60\2\2\u0241v\3")
        buf.write("\2\2\2\u0242\u0243\7/\2\2\u0243x\3\2\2\2\u0244\u0245\7")
        buf.write("/\2\2\u0245\u0246\7\60\2\2\u0246z\3\2\2\2\u0247\u0248")
        buf.write("\7,\2\2\u0248|\3\2\2\2\u0249\u024a\7,\2\2\u024a\u024b")
        buf.write("\7\60\2\2\u024b~\3\2\2\2\u024c\u024d\7^\2\2\u024d\u0080")
        buf.write("\3\2\2\2\u024e\u024f\7^\2\2\u024f\u0250\7\60\2\2\u0250")
        buf.write("\u0082\3\2\2\2\u0251\u0252\7\'\2\2\u0252\u0084\3\2\2\2")
        buf.write("\u0253\u0254\7#\2\2\u0254\u0086\3\2\2\2\u0255\u0256\7")
        buf.write("(\2\2\u0256\u0257\7(\2\2\u0257\u0088\3\2\2\2\u0258\u0259")
        buf.write("\7~\2\2\u0259\u025a\7~\2\2\u025a\u008a\3\2\2\2\u025b\u025c")
        buf.write("\7?\2\2\u025c\u025d\7?\2\2\u025d\u008c\3\2\2\2\u025e\u025f")
        buf.write("\7#\2\2\u025f\u0260\7?\2\2\u0260\u008e\3\2\2\2\u0261\u0262")
        buf.write("\7>\2\2\u0262\u0090\3\2\2\2\u0263\u0264\7@\2\2\u0264\u0092")
        buf.write("\3\2\2\2\u0265\u0266\7>\2\2\u0266\u0267\7?\2\2\u0267\u0094")
        buf.write("\3\2\2\2\u0268\u0269\7@\2\2\u0269\u026a\7?\2\2\u026a\u0096")
        buf.write("\3\2\2\2\u026b\u026c\7?\2\2\u026c\u026d\7^\2\2\u026d\u026e")
        buf.write("\7?\2\2\u026e\u0098\3\2\2\2\u026f\u0270\7>\2\2\u0270\u0271")
        buf.write("\7\60\2\2\u0271\u009a\3\2\2\2\u0272\u0273\7@\2\2\u0273")
        buf.write("\u0274\7\60\2\2\u0274\u009c\3\2\2\2\u0275\u0276\7>\2\2")
        buf.write("\u0276\u0277\7?\2\2\u0277\u0278\7\60\2\2\u0278\u009e\3")
        buf.write("\2\2\2\u0279\u027a\7@\2\2\u027a\u027b\7?\2\2\u027b\u027c")
        buf.write("\7\60\2\2\u027c\u00a0\3\2\2\2\u027d\u027e\7*\2\2\u027e")
        buf.write("\u00a2\3\2\2\2\u027f\u0280\7+\2\2\u0280\u00a4\3\2\2\2")
        buf.write("\u0281\u0282\7]\2\2\u0282\u00a6\3\2\2\2\u0283\u0284\7")
        buf.write("_\2\2\u0284\u00a8\3\2\2\2\u0285\u0286\7}\2\2\u0286\u00aa")
        buf.write("\3\2\2\2\u0287\u0288\7\177\2\2\u0288\u00ac\3\2\2\2\u0289")
        buf.write("\u028a\7<\2\2\u028a\u00ae\3\2\2\2\u028b\u028c\7\60\2\2")
        buf.write("\u028c\u00b0\3\2\2\2\u028d\u028e\7=\2\2\u028e\u00b2\3")
        buf.write("\2\2\2\u028f\u0290\7.\2\2\u0290\u00b4\3\2\2\2\u0291\u0292")
        buf.write("\7?\2\2\u0292\u00b6\3\2\2\2\u0293\u0294\7k\2\2\u0294\u0295")
        buf.write("\7p\2\2\u0295\u0296\7v\2\2\u0296\u0297\7a\2\2\u0297\u0298")
        buf.write("\7q\2\2\u0298\u0299\7h\2\2\u0299\u029a\7a\2\2\u029a\u029b")
        buf.write("\7h\2\2\u029b\u029c\7n\2\2\u029c\u029d\7q\2\2\u029d\u029e")
        buf.write("\7c\2\2\u029e\u029f\7v\2\2\u029f\u00b8\3\2\2\2\u02a0\u02a1")
        buf.write("\7k\2\2\u02a1\u02a2\7p\2\2\u02a2\u02a3\7v\2\2\u02a3\u02a4")
        buf.write("\7a\2\2\u02a4\u02a5\7q\2\2\u02a5\u02a6\7h\2\2\u02a6\u02a7")
        buf.write("\7a\2\2\u02a7\u02a8\7u\2\2\u02a8\u02a9\7v\2\2\u02a9\u02aa")
        buf.write("\7t\2\2\u02aa\u02ab\7k\2\2\u02ab\u02ac\7p\2\2\u02ac\u02ad")
        buf.write("\7i\2\2\u02ad\u00ba\3\2\2\2\u02ae\u02af\7h\2\2\u02af\u02b0")
        buf.write("\7n\2\2\u02b0\u02b1\7q\2\2\u02b1\u02b2\7c\2\2\u02b2\u02b3")
        buf.write("\7v\2\2\u02b3\u02b4\7a\2\2\u02b4\u02b5\7v\2\2\u02b5\u02b6")
        buf.write("\7q\2\2\u02b6\u02b7\7a\2\2\u02b7\u02b8\7k\2\2\u02b8\u02b9")
        buf.write("\7p\2\2\u02b9\u02ba\7v\2\2\u02ba\u00bc\3\2\2\2\u02bb\u02bc")
        buf.write("\7h\2\2\u02bc\u02bd\7n\2\2\u02bd\u02be\7q\2\2\u02be\u02bf")
        buf.write("\7c\2\2\u02bf\u02c0\7v\2\2\u02c0\u02c1\7a\2\2\u02c1\u02c2")
        buf.write("\7q\2\2\u02c2\u02c3\7h\2\2\u02c3\u02c4\7a\2\2\u02c4\u02c5")
        buf.write("\7u\2\2\u02c5\u02c6\7v\2\2\u02c6\u02c7\7t\2\2\u02c7\u02c8")
        buf.write("\7k\2\2\u02c8\u02c9\7p\2\2\u02c9\u02ca\7i\2\2\u02ca\u00be")
        buf.write("\3\2\2\2\u02cb\u02cc\7d\2\2\u02cc\u02cd\7q\2\2\u02cd\u02ce")
        buf.write("\7q\2\2\u02ce\u02cf\7n\2\2\u02cf\u02d0\7a\2\2\u02d0\u02d1")
        buf.write("\7q\2\2\u02d1\u02d2\7h\2\2\u02d2\u02d3\7a\2\2\u02d3\u02d4")
        buf.write("\7u\2\2\u02d4\u02d5\7v\2\2\u02d5\u02d6\7t\2\2\u02d6\u02d7")
        buf.write("\7k\2\2\u02d7\u02d8\7p\2\2\u02d8\u02d9\7i\2\2\u02d9\u00c0")
        buf.write("\3\2\2\2\u02da\u02db\7u\2\2\u02db\u02dc\7v\2\2\u02dc\u02dd")
        buf.write("\7t\2\2\u02dd\u02de\7k\2\2\u02de\u02df\7p\2\2\u02df\u02e0")
        buf.write("\7i\2\2\u02e0\u02e1\7a\2\2\u02e1\u02e2\7q\2\2\u02e2\u02e3")
        buf.write("\7h\2\2\u02e3\u02e4\7a\2\2\u02e4\u02e5\7d\2\2\u02e5\u02e6")
        buf.write("\7q\2\2\u02e6\u02e7\7q\2\2\u02e7\u02e8\7n\2\2\u02e8\u00c2")
        buf.write("\3\2\2\2\u02e9\u02ea\7u\2\2\u02ea\u02eb\7v\2\2\u02eb\u02ec")
        buf.write("\7t\2\2\u02ec\u02ed\7k\2\2\u02ed\u02ee\7p\2\2\u02ee\u02ef")
        buf.write("\7i\2\2\u02ef\u02f0\7a\2\2\u02f0\u02f1\7q\2\2\u02f1\u02f2")
        buf.write("\7h\2\2\u02f2\u02f3\7a\2\2\u02f3\u02f4\7k\2\2\u02f4\u02f5")
        buf.write("\7p\2\2\u02f5\u02f6\7v\2\2\u02f6\u00c4\3\2\2\2\u02f7\u02f8")
        buf.write("\7u\2\2\u02f8\u02f9\7v\2\2\u02f9\u02fa\7t\2\2\u02fa\u02fb")
        buf.write("\7k\2\2\u02fb\u02fc\7p\2\2\u02fc\u02fd\7i\2\2\u02fd\u02fe")
        buf.write("\7a\2\2\u02fe\u02ff\7q\2\2\u02ff\u0300\7h\2\2\u0300\u0301")
        buf.write("\7a\2\2\u0301\u0302\7h\2\2\u0302\u0303\7n\2\2\u0303\u0304")
        buf.write("\7q\2\2\u0304\u0305\7c\2\2\u0305\u0306\7v\2\2\u0306\u00c6")
        buf.write("\3\2\2\2$\2\u00d6\u00db\u00e4\u00f0\u00fc\u0103\u0107")
        buf.write("\u010b\u0110\u0112\u0119\u0122\u0126\u0130\u013e\u0140")
        buf.write("\u014a\u0156\u015a\u015f\u0165\u016b\u016f\u0172\u0180")
        buf.write("\u018a\u018f\u0194\u019a\u019f\u01a4\u01aa\u01b0\5\3\f")
        buf.write("\2\b\2\2\3$\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    ARRAY_LIT = 2
    INT_ARRAY = 3
    FLOAT_ARRAY = 4
    STRING_ARRAY = 5
    ID = 6
    ILLEGAL_ESCAPE = 7
    UNCLOSE_STRING = 8
    COMMENT = 9
    UNTERMINATED_COMMENT = 10
    ERROR_CHAR = 11
    WS = 12
    Integer_literal = 13
    Float_literal = 14
    Boolean_literal = 15
    String_literal = 16
    BODY = 17
    BREAK = 18
    CONTINUE = 19
    DO = 20
    ELSE = 21
    ELSEIF = 22
    ENDIF = 23
    ENDBODY = 24
    ENDFOR = 25
    ENDWHILE = 26
    FOR = 27
    FUNCTION = 28
    IF = 29
    PARAMETER = 30
    RETURN = 31
    THEN = 32
    VAR = 33
    WHILE = 34
    TRUE = 35
    FALSE = 36
    ENDDO = 37
    PLUS_INT = 38
    PLUS_FLOAT = 39
    MINUS_INT = 40
    MINUS_FLOAT = 41
    STAR_INT = 42
    STAR_FLOAT = 43
    DIV_INT = 44
    DIV_FLOAT = 45
    MOD = 46
    NOT = 47
    AND = 48
    OR = 49
    EQUAL = 50
    NOT_EQUAL_INT = 51
    LESS_INT = 52
    GREATER_INT = 53
    LESS_OR_EQUAL_INT = 54
    GREATER_OR_EQUAL_INT = 55
    NOT_EQUAL_FLOAT = 56
    LESS_FLOAT = 57
    GREATER_FLOAT = 58
    LESS_OR_EQUAL_FLOAT = 59
    GREATER_OR_EQUAL_FLOAT = 60
    LEFT_PAREN = 61
    RIGHT_PAREN = 62
    LEFT_BRACKET = 63
    RIGHT_BRACKET = 64
    LEFT_BRACE = 65
    RIGHT_BRACE = 66
    COLON = 67
    DOT = 68
    SEMI = 69
    COMMA = 70
    ASSIGN = 71
    INT_OF_FLOAT = 72
    INT_OF_STRING = 73
    FLOAT_TO_INT = 74
    FLOAT_OF_STRING = 75
    BOOL_OF_STRING = 76
    STRING_OF_BOOL = 77
    STRING_OF_INT = 78
    STRING_OF_FLOAT = 79

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndIf.'", "'EndBody.'", "'EndFor.'", "'EndWhile.'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'EndDo.'", "'+'", 
            "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", 
            "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", 
            "'>='", "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", "','", "'='", 
            "'int_of_float'", "'int_of_string'", "'float_to_int'", "'float_of_string'", 
            "'bool_of_string'", "'string_of_bool'", "'string_of_int'", "'string_of_float'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY_LIT", "INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", "ID", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
            "ERROR_CHAR", "WS", "Integer_literal", "Float_literal", "Boolean_literal", 
            "String_literal", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
            "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", 
            "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", 
            "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", 
            "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", 
            "LEFT_BRACE", "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", 
            "ASSIGN", "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_TO_INT", "FLOAT_OF_STRING", 
            "BOOL_OF_STRING", "STRING_OF_BOOL", "STRING_OF_INT", "STRING_OF_FLOAT" ]

    ruleNames = [ "T__0", "ARRAY_LIT", "INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", 
                  "INT_ELEMENT", "FLOAT_ELEMENT", "STRING_ELEMENT", "ID", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR", "WS", "LOWERCASE_LETTER", "UPPERCASE_LETTER", 
                  "DIGIT", "LETTER", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
                  "ILL_ESC_SEQUENCE", "SUP_ESC_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", 
                  "STRING_CHAR", "HEXADECIMALDIGIT", "OCTALDIGIT", "HEXADECIMAL", 
                  "DECIMAL", "OCTAL", "Integer_literal", "Float_literal", 
                  "Boolean_literal", "String_literal", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                  "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
                  "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                  "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
                  "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PAREN", 
                  "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                  "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "INT_OF_FLOAT", 
                  "INT_OF_STRING", "FLOAT_TO_INT", "FLOAT_OF_STRING", "BOOL_OF_STRING", 
                  "STRING_OF_BOOL", "STRING_OF_INT", "STRING_OF_FLOAT" ]

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
            actions[10] = self.UNCLOSE_STRING_action 
            actions[34] = self.String_literal_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = str(self.text)
                    self.text = y[1:]
                
     

    def String_literal_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     


