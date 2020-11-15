# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H")
        buf.write("\u025c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\3\2\6\2\u00ad\n\2\r\2\16\2\u00ae\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\7\3\u00b7\n\3\f\3\16\3\u00ba\13\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00cc")
        buf.write("\n\4\3\5\3\5\3\5\3\5\5\5\u00d2\n\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\5\6\u00d9\n\6\3\7\3\7\5\7\u00dd\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\7\b\u00e4\n\b\f\b\16\b\u00e7\13\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\7\23\u00ff\n\23\f\23\16")
        buf.write("\23\u0102\13\23\3\23\3\23\3\23\7\23\u0107\n\23\f\23\16")
        buf.write("\23\u010a\13\23\3\23\3\23\3\23\7\23\u010f\n\23\f\23\16")
        buf.write("\23\u0112\13\23\3\23\5\23\u0115\n\23\3\24\6\24\u0118\n")
        buf.write("\24\r\24\16\24\u0119\3\24\3\24\7\24\u011e\n\24\f\24\16")
        buf.write("\24\u0121\13\24\3\24\5\24\u0124\n\24\3\24\5\24\u0127\n")
        buf.write("\24\3\25\3\25\5\25\u012b\n\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3")
        buf.write("B\3B\3B\3B\3B\3B\3C\3C\3D\3D\7D\u01f5\nD\fD\16D\u01f8")
        buf.write("\13D\3D\5D\u01fb\nD\3D\3D\3E\3E\7E\u0201\nE\fE\16E\u0204")
        buf.write("\13E\3E\3E\3E\3F\3F\3F\3F\7F\u020d\nF\fF\16F\u0210\13")
        buf.write("F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3K\3L\5L\u021e\nL\3M\3")
        buf.write("M\6M\u0222\nM\rM\16M\u0223\3N\3N\3N\3N\5N\u022a\nN\3O")
        buf.write("\3O\3O\3O\5O\u0230\nO\3P\3P\3P\3Q\3Q\3R\3R\3R\3R\3R\3")
        buf.write("R\3R\3R\3R\3R\3R\3R\3R\3R\5R\u0245\nR\3S\3S\3S\3S\5S\u024b")
        buf.write("\nS\3T\3T\3T\3T\5T\u0251\nT\3U\3U\7U\u0255\nU\fU\16U\u0258")
        buf.write("\13U\3U\3U\3U\4\u00b8\u020e\2V\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f")
        buf.write("\2\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9H\3\2\21\5\2\13")
        buf.write("\f\17\17\"\"\3\2\63;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\62")
        buf.write("9\3\3\f\f\3\2c|\3\2C\\\3\2\62;\4\2GGgg\4\2--//\t\2))^")
        buf.write("^ddhhppttvv\3\2$$\6\2\f\f$$))^^\2\u0281\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u00a9\3\2\2\2\3\u00ac\3\2\2\2\5\u00b2\3\2\2")
        buf.write("\2\7\u00cb\3\2\2\2\t\u00d1\3\2\2\2\13\u00d8\3\2\2\2\r")
        buf.write("\u00dc\3\2\2\2\17\u00de\3\2\2\2\21\u00e8\3\2\2\2\23\u00ea")
        buf.write("\3\2\2\2\25\u00ec\3\2\2\2\27\u00ee\3\2\2\2\31\u00f0\3")
        buf.write("\2\2\2\33\u00f2\3\2\2\2\35\u00f4\3\2\2\2\37\u00f6\3\2")
        buf.write("\2\2!\u00f8\3\2\2\2#\u00fa\3\2\2\2%\u0114\3\2\2\2\'\u0117")
        buf.write("\3\2\2\2)\u012a\3\2\2\2+\u012c\3\2\2\2-\u012f\3\2\2\2")
        buf.write("/\u0131\3\2\2\2\61\u0134\3\2\2\2\63\u0136\3\2\2\2\65\u0139")
        buf.write("\3\2\2\2\67\u013b\3\2\2\29\u013e\3\2\2\2;\u0140\3\2\2")
        buf.write("\2=\u0142\3\2\2\2?\u0145\3\2\2\2A\u0149\3\2\2\2C\u014d")
        buf.write("\3\2\2\2E\u0151\3\2\2\2G\u0154\3\2\2\2I\u0157\3\2\2\2")
        buf.write("K\u015a\3\2\2\2M\u015d\3\2\2\2O\u0160\3\2\2\2Q\u0162\3")
        buf.write("\2\2\2S\u0164\3\2\2\2U\u0166\3\2\2\2W\u0169\3\2\2\2Y\u016c")
        buf.write("\3\2\2\2[\u016e\3\2\2\2]\u0172\3\2\2\2_\u017b\3\2\2\2")
        buf.write("a\u0180\3\2\2\2c\u0185\3\2\2\2e\u018c\3\2\2\2g\u018f\3")
        buf.write("\2\2\2i\u0195\3\2\2\2k\u019b\3\2\2\2m\u01a2\3\2\2\2o\u01ab")
        buf.write("\3\2\2\2q\u01b5\3\2\2\2s\u01bb\3\2\2\2u\u01c4\3\2\2\2")
        buf.write("w\u01cc\3\2\2\2y\u01d0\3\2\2\2{\u01d7\3\2\2\2}\u01dc\3")
        buf.write("\2\2\2\177\u01df\3\2\2\2\u0081\u01e5\3\2\2\2\u0083\u01ea")
        buf.write("\3\2\2\2\u0085\u01f0\3\2\2\2\u0087\u01f2\3\2\2\2\u0089")
        buf.write("\u01fe\3\2\2\2\u008b\u0208\3\2\2\2\u008d\u0211\3\2\2\2")
        buf.write("\u008f\u0213\3\2\2\2\u0091\u0215\3\2\2\2\u0093\u0217\3")
        buf.write("\2\2\2\u0095\u0219\3\2\2\2\u0097\u021d\3\2\2\2\u0099\u021f")
        buf.write("\3\2\2\2\u009b\u0229\3\2\2\2\u009d\u022f\3\2\2\2\u009f")
        buf.write("\u0231\3\2\2\2\u00a1\u0234\3\2\2\2\u00a3\u0244\3\2\2\2")
        buf.write("\u00a5\u024a\3\2\2\2\u00a7\u0250\3\2\2\2\u00a9\u0252\3")
        buf.write("\2\2\2\u00ab\u00ad\t\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b1\b\2\2\2\u00b1\4\3\2\2\2\u00b2")
        buf.write("\u00b3\7,\2\2\u00b3\u00b4\7,\2\2\u00b4\u00b8\3\2\2\2\u00b5")
        buf.write("\u00b7\13\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2")
        buf.write("\2\u00b8\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bb")
        buf.write("\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7,\2\2\u00bc")
        buf.write("\u00bd\7,\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\b\3\2\2")
        buf.write("\u00bf\6\3\2\2\2\u00c0\u00cc\5=\37\2\u00c1\u00cc\5? \2")
        buf.write("\u00c2\u00cc\5A!\2\u00c3\u00cc\5C\"\2\u00c4\u00cc\5E#")
        buf.write("\2\u00c5\u00cc\5G$\2\u00c6\u00cc\5I%\2\u00c7\u00cc\5K")
        buf.write("&\2\u00c8\u00cc\5M\'\2\u00c9\u00cc\5O(\2\u00ca\u00cc\5")
        buf.write("Q)\2\u00cb\u00c0\3\2\2\2\u00cb\u00c1\3\2\2\2\u00cb\u00c2")
        buf.write("\3\2\2\2\u00cb\u00c3\3\2\2\2\u00cb\u00c4\3\2\2\2\u00cb")
        buf.write("\u00c5\3\2\2\2\u00cb\u00c6\3\2\2\2\u00cb\u00c7\3\2\2\2")
        buf.write("\u00cb\u00c8\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3")
        buf.write("\2\2\2\u00cc\b\3\2\2\2\u00cd\u00d2\5+\26\2\u00ce\u00d2")
        buf.write("\5/\30\2\u00cf\u00d2\5-\27\2\u00d0\u00d2\5\61\31\2\u00d1")
        buf.write("\u00cd\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d0\3\2\2\2\u00d2\n\3\2\2\2\u00d3\u00d9\5\63")
        buf.write("\32\2\u00d4\u00d9\5\67\34\2\u00d5\u00d9\5\65\33\2\u00d6")
        buf.write("\u00d9\59\35\2\u00d7\u00d9\5;\36\2\u00d8\u00d3\3\2\2\2")
        buf.write("\u00d8\u00d4\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d8\u00d6\3")
        buf.write("\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\f\3\2\2\2\u00da\u00dd")
        buf.write("\5\61\31\2\u00db\u00dd\5/\30\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\16\3\2\2\2\u00de\u00e5\5\u008fH\2")
        buf.write("\u00df\u00e4\5\u008fH\2\u00e0\u00e4\5\u0091I\2\u00e1\u00e4")
        buf.write("\5\u0093J\2\u00e2\u00e4\7a\2\2\u00e3\u00df\3\2\2\2\u00e3")
        buf.write("\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3")
        buf.write("\2\2\2\u00e6\20\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9")
        buf.write("\7}\2\2\u00e9\22\3\2\2\2\u00ea\u00eb\7\177\2\2\u00eb\24")
        buf.write("\3\2\2\2\u00ec\u00ed\7]\2\2\u00ed\26\3\2\2\2\u00ee\u00ef")
        buf.write("\7_\2\2\u00ef\30\3\2\2\2\u00f0\u00f1\7*\2\2\u00f1\32\3")
        buf.write("\2\2\2\u00f2\u00f3\7+\2\2\u00f3\34\3\2\2\2\u00f4\u00f5")
        buf.write("\7=\2\2\u00f5\36\3\2\2\2\u00f6\u00f7\7<\2\2\u00f7 \3\2")
        buf.write("\2\2\u00f8\u00f9\7.\2\2\u00f9\"\3\2\2\2\u00fa\u00fb\7")
        buf.write("\60\2\2\u00fb$\3\2\2\2\u00fc\u0100\t\3\2\2\u00fd\u00ff")
        buf.write("\5\u0093J\2\u00fe\u00fd\3\2\2\2\u00ff\u0102\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0115\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0103\u0104\5\u009bN\2\u0104\u0108")
        buf.write("\t\4\2\2\u0105\u0107\t\5\2\2\u0106\u0105\3\2\2\2\u0107")
        buf.write("\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u0115\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\5")
        buf.write("\u009dO\2\u010c\u0110\t\6\2\2\u010d\u010f\t\7\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\u0115\3\2\2\2\u0112\u0110\3")
        buf.write("\2\2\2\u0113\u0115\7\62\2\2\u0114\u00fc\3\2\2\2\u0114")
        buf.write("\u0103\3\2\2\2\u0114\u010b\3\2\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115&\3\2\2\2\u0116\u0118\5\u0093J\2\u0117\u0116\3\2")
        buf.write("\2\2\u0118\u0119\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u0126\3\2\2\2\u011b\u011f\5#\22\2\u011c")
        buf.write("\u011e\5\u0093J\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2")
        buf.write("\2\2\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0123")
        buf.write("\3\2\2\2\u0121\u011f\3\2\2\2\u0122\u0124\5\u0099M\2\u0123")
        buf.write("\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0127\3\2\2\2")
        buf.write("\u0125\u0127\5\u0099M\2\u0126\u011b\3\2\2\2\u0126\u0125")
        buf.write("\3\2\2\2\u0127(\3\2\2\2\u0128\u012b\5{>\2\u0129\u012b")
        buf.write("\5\u0083B\2\u012a\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b")
        buf.write("*\3\2\2\2\u012c\u012d\7-\2\2\u012d\u012e\7\60\2\2\u012e")
        buf.write(",\3\2\2\2\u012f\u0130\7-\2\2\u0130.\3\2\2\2\u0131\u0132")
        buf.write("\7/\2\2\u0132\u0133\7\60\2\2\u0133\60\3\2\2\2\u0134\u0135")
        buf.write("\7/\2\2\u0135\62\3\2\2\2\u0136\u0137\7,\2\2\u0137\u0138")
        buf.write("\7\60\2\2\u0138\64\3\2\2\2\u0139\u013a\7,\2\2\u013a\66")
        buf.write("\3\2\2\2\u013b\u013c\7^\2\2\u013c\u013d\7\60\2\2\u013d")
        buf.write("8\3\2\2\2\u013e\u013f\7^\2\2\u013f:\3\2\2\2\u0140\u0141")
        buf.write("\7\'\2\2\u0141<\3\2\2\2\u0142\u0143\7?\2\2\u0143\u0144")
        buf.write("\7?\2\2\u0144>\3\2\2\2\u0145\u0146\7?\2\2\u0146\u0147")
        buf.write("\7\61\2\2\u0147\u0148\7?\2\2\u0148@\3\2\2\2\u0149\u014a")
        buf.write("\7>\2\2\u014a\u014b\7?\2\2\u014b\u014c\7\60\2\2\u014c")
        buf.write("B\3\2\2\2\u014d\u014e\7@\2\2\u014e\u014f\7?\2\2\u014f")
        buf.write("\u0150\7\60\2\2\u0150D\3\2\2\2\u0151\u0152\7>\2\2\u0152")
        buf.write("\u0153\7\60\2\2\u0153F\3\2\2\2\u0154\u0155\7@\2\2\u0155")
        buf.write("\u0156\7\60\2\2\u0156H\3\2\2\2\u0157\u0158\7#\2\2\u0158")
        buf.write("\u0159\7?\2\2\u0159J\3\2\2\2\u015a\u015b\7>\2\2\u015b")
        buf.write("\u015c\7?\2\2\u015cL\3\2\2\2\u015d\u015e\7@\2\2\u015e")
        buf.write("\u015f\7?\2\2\u015fN\3\2\2\2\u0160\u0161\7>\2\2\u0161")
        buf.write("P\3\2\2\2\u0162\u0163\7@\2\2\u0163R\3\2\2\2\u0164\u0165")
        buf.write("\7#\2\2\u0165T\3\2\2\2\u0166\u0167\7(\2\2\u0167\u0168")
        buf.write("\7(\2\2\u0168V\3\2\2\2\u0169\u016a\7~\2\2\u016a\u016b")
        buf.write("\7~\2\2\u016bX\3\2\2\2\u016c\u016d\7?\2\2\u016dZ\3\2\2")
        buf.write("\2\u016e\u016f\7X\2\2\u016f\u0170\7c\2\2\u0170\u0171\7")
        buf.write("t\2\2\u0171\\\3\2\2\2\u0172\u0173\7H\2\2\u0173\u0174\7")
        buf.write("w\2\2\u0174\u0175\7p\2\2\u0175\u0176\7e\2\2\u0176\u0177")
        buf.write("\7v\2\2\u0177\u0178\7k\2\2\u0178\u0179\7q\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a^\3\2\2\2\u017b\u017c\7D\2\2\u017c\u017d")
        buf.write("\7q\2\2\u017d\u017e\7f\2\2\u017e\u017f\7{\2\2\u017f`\3")
        buf.write("\2\2\2\u0180\u0181\7G\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7u\2\2\u0183\u0184\7g\2\2\u0184b\3\2\2\2\u0185\u0186")
        buf.write("\7G\2\2\u0186\u0187\7p\2\2\u0187\u0188\7f\2\2\u0188\u0189")
        buf.write("\7H\2\2\u0189\u018a\7q\2\2\u018a\u018b\7t\2\2\u018bd\3")
        buf.write("\2\2\2\u018c\u018d\7K\2\2\u018d\u018e\7h\2\2\u018ef\3")
        buf.write("\2\2\2\u018f\u0190\7G\2\2\u0190\u0191\7p\2\2\u0191\u0192")
        buf.write("\7f\2\2\u0192\u0193\7F\2\2\u0193\u0194\7q\2\2\u0194h\3")
        buf.write("\2\2\2\u0195\u0196\7D\2\2\u0196\u0197\7t\2\2\u0197\u0198")
        buf.write("\7g\2\2\u0198\u0199\7c\2\2\u0199\u019a\7m\2\2\u019aj\3")
        buf.write("\2\2\2\u019b\u019c\7G\2\2\u019c\u019d\7n\2\2\u019d\u019e")
        buf.write("\7u\2\2\u019e\u019f\7g\2\2\u019f\u01a0\7K\2\2\u01a0\u01a1")
        buf.write("\7h\2\2\u01a1l\3\2\2\2\u01a2\u01a3\7G\2\2\u01a3\u01a4")
        buf.write("\7p\2\2\u01a4\u01a5\7f\2\2\u01a5\u01a6\7Y\2\2\u01a6\u01a7")
        buf.write("\7j\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9\7n\2\2\u01a9\u01aa")
        buf.write("\7g\2\2\u01aan\3\2\2\2\u01ab\u01ac\7R\2\2\u01ac\u01ad")
        buf.write("\7c\2\2\u01ad\u01ae\7t\2\2\u01ae\u01af\7c\2\2\u01af\u01b0")
        buf.write("\7o\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2\7v\2\2\u01b2\u01b3")
        buf.write("\7g\2\2\u01b3\u01b4\7t\2\2\u01b4p\3\2\2\2\u01b5\u01b6")
        buf.write("\7Y\2\2\u01b6\u01b7\7j\2\2\u01b7\u01b8\7k\2\2\u01b8\u01b9")
        buf.write("\7n\2\2\u01b9\u01ba\7g\2\2\u01bar\3\2\2\2\u01bb\u01bc")
        buf.write("\7E\2\2\u01bc\u01bd\7q\2\2\u01bd\u01be\7p\2\2\u01be\u01bf")
        buf.write("\7v\2\2\u01bf\u01c0\7k\2\2\u01c0\u01c1\7p\2\2\u01c1\u01c2")
        buf.write("\7w\2\2\u01c2\u01c3\7g\2\2\u01c3t\3\2\2\2\u01c4\u01c5")
        buf.write("\7G\2\2\u01c5\u01c6\7p\2\2\u01c6\u01c7\7f\2\2\u01c7\u01c8")
        buf.write("\7D\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca\7f\2\2\u01ca\u01cb")
        buf.write("\7{\2\2\u01cbv\3\2\2\2\u01cc\u01cd\7H\2\2\u01cd\u01ce")
        buf.write("\7q\2\2\u01ce\u01cf\7t\2\2\u01cfx\3\2\2\2\u01d0\u01d1")
        buf.write("\7T\2\2\u01d1\u01d2\7g\2\2\u01d2\u01d3\7v\2\2\u01d3\u01d4")
        buf.write("\7w\2\2\u01d4\u01d5\7t\2\2\u01d5\u01d6\7p\2\2\u01d6z\3")
        buf.write("\2\2\2\u01d7\u01d8\7V\2\2\u01d8\u01d9\7t\2\2\u01d9\u01da")
        buf.write("\7w\2\2\u01da\u01db\7g\2\2\u01db|\3\2\2\2\u01dc\u01dd")
        buf.write("\7F\2\2\u01dd\u01de\7q\2\2\u01de~\3\2\2\2\u01df\u01e0")
        buf.write("\7G\2\2\u01e0\u01e1\7p\2\2\u01e1\u01e2\7f\2\2\u01e2\u01e3")
        buf.write("\7K\2\2\u01e3\u01e4\7h\2\2\u01e4\u0080\3\2\2\2\u01e5\u01e6")
        buf.write("\7V\2\2\u01e6\u01e7\7j\2\2\u01e7\u01e8\7g\2\2\u01e8\u01e9")
        buf.write("\7p\2\2\u01e9\u0082\3\2\2\2\u01ea\u01eb\7H\2\2\u01eb\u01ec")
        buf.write("\7c\2\2\u01ec\u01ed\7n\2\2\u01ed\u01ee\7u\2\2\u01ee\u01ef")
        buf.write("\7g\2\2\u01ef\u0084\3\2\2\2\u01f0\u01f1\13\2\2\2\u01f1")
        buf.write("\u0086\3\2\2\2\u01f2\u01f6\5\u008dG\2\u01f3\u01f5\5\u00a7")
        buf.write("T\2\u01f4\u01f3\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f9\u01fb\t\b\2\2\u01fa\u01f9\3\2\2\2")
        buf.write("\u01fb\u01fc\3\2\2\2\u01fc\u01fd\bD\3\2\u01fd\u0088\3")
        buf.write("\2\2\2\u01fe\u0202\7$\2\2\u01ff\u0201\5\u00a7T\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3")
        buf.write("\2\2\2\u0205\u0206\5\u00a5S\2\u0206\u0207\bE\4\2\u0207")
        buf.write("\u008a\3\2\2\2\u0208\u0209\7,\2\2\u0209\u020a\7,\2\2\u020a")
        buf.write("\u020e\3\2\2\2\u020b\u020d\13\2\2\2\u020c\u020b\3\2\2")
        buf.write("\2\u020d\u0210\3\2\2\2\u020e\u020f\3\2\2\2\u020e\u020c")
        buf.write("\3\2\2\2\u020f\u008c\3\2\2\2\u0210\u020e\3\2\2\2\u0211")
        buf.write("\u0212\7$\2\2\u0212\u008e\3\2\2\2\u0213\u0214\t\t\2\2")
        buf.write("\u0214\u0090\3\2\2\2\u0215\u0216\t\n\2\2\u0216\u0092\3")
        buf.write("\2\2\2\u0217\u0218\t\13\2\2\u0218\u0094\3\2\2\2\u0219")
        buf.write("\u021a\t\f\2\2\u021a\u021b\5\u0097L\2\u021b\u0096\3\2")
        buf.write("\2\2\u021c\u021e\t\r\2\2\u021d\u021c\3\2\2\2\u021d\u021e")
        buf.write("\3\2\2\2\u021e\u0098\3\2\2\2\u021f\u0221\5\u0095K\2\u0220")
        buf.write("\u0222\5\u0093J\2\u0221\u0220\3\2\2\2\u0222\u0223\3\2")
        buf.write("\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u009a")
        buf.write("\3\2\2\2\u0225\u0226\7\62\2\2\u0226\u022a\7z\2\2\u0227")
        buf.write("\u0228\7\62\2\2\u0228\u022a\7Z\2\2\u0229\u0225\3\2\2\2")
        buf.write("\u0229\u0227\3\2\2\2\u022a\u009c\3\2\2\2\u022b\u022c\7")
        buf.write("\62\2\2\u022c\u0230\7q\2\2\u022d\u022e\7\62\2\2\u022e")
        buf.write("\u0230\7Q\2\2\u022f\u022b\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u0230\u009e\3\2\2\2\u0231\u0232\5\u00a1Q\2\u0232\u0233")
        buf.write("\5\u008dG\2\u0233\u00a0\3\2\2\2\u0234\u0235\7)\2\2\u0235")
        buf.write("\u00a2\3\2\2\2\u0236\u0237\7^\2\2\u0237\u0245\7d\2\2\u0238")
        buf.write("\u0239\7^\2\2\u0239\u0245\7h\2\2\u023a\u023b\7^\2\2\u023b")
        buf.write("\u0245\7t\2\2\u023c\u023d\7^\2\2\u023d\u0245\7p\2\2\u023e")
        buf.write("\u023f\7^\2\2\u023f\u0245\7v\2\2\u0240\u0241\7^\2\2\u0241")
        buf.write("\u0245\7)\2\2\u0242\u0243\7^\2\2\u0243\u0245\7^\2\2\u0244")
        buf.write("\u0236\3\2\2\2\u0244\u0238\3\2\2\2\u0244\u023a\3\2\2\2")
        buf.write("\u0244\u023c\3\2\2\2\u0244\u023e\3\2\2\2\u0244\u0240\3")
        buf.write("\2\2\2\u0244\u0242\3\2\2\2\u0245\u00a4\3\2\2\2\u0246\u0247")
        buf.write("\7^\2\2\u0247\u024b\n\16\2\2\u0248\u0249\7)\2\2\u0249")
        buf.write("\u024b\n\17\2\2\u024a\u0246\3\2\2\2\u024a\u0248\3\2\2")
        buf.write("\2\u024b\u00a6\3\2\2\2\u024c\u0251\5\u00a3R\2\u024d\u024e")
        buf.write("\7)\2\2\u024e\u0251\7$\2\2\u024f\u0251\n\20\2\2\u0250")
        buf.write("\u024c\3\2\2\2\u0250\u024d\3\2\2\2\u0250\u024f\3\2\2\2")
        buf.write("\u0251\u00a8\3\2\2\2\u0252\u0256\5\u008dG\2\u0253\u0255")
        buf.write("\5\u00a7T\2\u0254\u0253\3\2\2\2\u0255\u0258\3\2\2\2\u0256")
        buf.write("\u0254\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0259\3\2\2\2")
        buf.write("\u0258\u0256\3\2\2\2\u0259\u025a\5\u008dG\2\u025a\u025b")
        buf.write("\bU\5\2\u025b\u00aa\3\2\2\2 \2\u00ae\u00b8\u00cb\u00d1")
        buf.write("\u00d8\u00dc\u00e3\u00e5\u0100\u0108\u0110\u0114\u0119")
        buf.write("\u011f\u0123\u0126\u012a\u01f6\u01fa\u0202\u020e\u021d")
        buf.write("\u0223\u0229\u022f\u0244\u024a\u0250\u0256\6\b\2\2\3D")
        buf.write("\2\3E\3\3U\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT = 2
    RELATION_OP = 3
    ADDSUB = 4
    MULDIV = 5
    NEGSIGN = 6
    IDENTIFIER = 7
    LB = 8
    RB = 9
    LK = 10
    RK = 11
    LP = 12
    RP = 13
    SEMI = 14
    COLON = 15
    CM = 16
    DOT = 17
    INTEGER = 18
    FLOAT = 19
    BOLEAN = 20
    FADDOP = 21
    IADDOP = 22
    FSUBOP = 23
    ISUBOP = 24
    FMULOP = 25
    IMULOP = 26
    FDIVOP = 27
    IDIVOP = 28
    IREMAIN = 29
    EQUAL = 30
    FNEQUAL = 31
    FLESSOE = 32
    FGROE = 33
    FLESS = 34
    FGR = 35
    INEQUAL = 36
    ILESSOE = 37
    IGROE = 38
    ILESS = 39
    IGR = 40
    BNEG = 41
    BAND = 42
    BOR = 43
    AS = 44
    VAR = 45
    FUNCTION = 46
    BODY = 47
    ELSE = 48
    ENDFOR = 49
    IF = 50
    ENDDO = 51
    BREAK = 52
    ELSEIF = 53
    ENDWHILE = 54
    PARAMETER = 55
    WHILE = 56
    CONTINUE = 57
    ENDBODY = 58
    FOR = 59
    RETURN = 60
    TRUE = 61
    DO = 62
    ENDIF = 63
    THEN = 64
    FALSE = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68
    UNTERMINATED_COMMENT = 69
    LSTRING = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'['", "']'", "'('", "')'", "';'", "':'", "','", 
            "'.'", "'+.'", "'+'", "'-.'", "'-'", "'*.'", "'*'", "'\\.'", 
            "'\\'", "'%'", "'=='", "'=/='", "'<=.'", "'>=.'", "'<.'", "'>.'", 
            "'!='", "'<='", "'>='", "'<'", "'>'", "'!'", "'&&'", "'||'", 
            "'='", "'Var'", "'Function'", "'Body'", "'Else'", "'EndFor'", 
            "'If'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", 
            "'While'", "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", 
            "'Do'", "'EndIf'", "'Then'", "'False'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT", "RELATION_OP", "ADDSUB", "MULDIV", "NEGSIGN", 
            "IDENTIFIER", "LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", 
            "CM", "DOT", "INTEGER", "FLOAT", "BOLEAN", "FADDOP", "IADDOP", 
            "FSUBOP", "ISUBOP", "FMULOP", "IMULOP", "FDIVOP", "IDIVOP", 
            "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", "FGROE", "FLESS", 
            "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", "BNEG", 
            "BAND", "BOR", "AS", "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", 
            "IF", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", 
            "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", 
            "THEN", "FALSE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT", "LSTRING" ]

    ruleNames = [ "WS", "COMMENT", "RELATION_OP", "ADDSUB", "MULDIV", "NEGSIGN", 
                  "IDENTIFIER", "LB", "RB", "LK", "RK", "LP", "RP", "SEMI", 
                  "COLON", "CM", "DOT", "INTEGER", "FLOAT", "BOLEAN", "FADDOP", 
                  "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", "IMULOP", "FDIVOP", 
                  "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", "FGROE", 
                  "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", 
                  "IGR", "BNEG", "BAND", "BOR", "AS", "VAR", "FUNCTION", 
                  "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", "ELSEIF", 
                  "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", 
                  "FOR", "RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "DOUQUO", "LETTER", "UPCASE_LETTER", "NUMBER", "EXPO", 
                  "SIGN", "SCIEN", "HEX", "OCTA", "SDOUQUO", "SINGQUO", 
                  "ESCAPE_CHAR", "ILLEGAL_CHAR", "CHAR_STRING", "LSTRING" ]

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
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[83] = self.LSTRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = (self.text)[1:]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = (self.text)[1:]

     

    def LSTRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = self.text[1:-1] 
     


