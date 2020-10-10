# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0229\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\7\3\u00b0\n\3\f\3\16\3\u00b3\13\3")
        buf.write("\3\4\3\4\7\4\u00b7\n\4\f\4\16\4\u00ba\13\4\3\4\3\4\3\5")
        buf.write("\3\5\7\5\u00c0\n\5\f\5\16\5\u00c3\13\5\3\5\5\5\u00c6\n")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6\u00ce\n\6\f\6\16\6\u00d1")
        buf.write("\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00dc\n")
        buf.write("\7\f\7\16\7\u00df\13\7\3\7\3\7\3\b\3\b\3\t\6\t\u00e6\n")
        buf.write("\t\r\t\16\t\u00e7\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\5\r\u00f4\n\r\3\16\5\16\u00f7\n\16\3\17\3\17\3")
        buf.write("\17\6\17\u00fc\n\17\r\17\16\17\u00fd\3\20\3\20\7\20\u0102")
        buf.write("\n\20\f\20\16\20\u0105\13\20\3\21\6\21\u0108\n\21\r\21")
        buf.write("\16\21\u0109\3\21\3\21\5\21\u010e\n\21\3\21\5\21\u0111")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\5\25\u011f\n\25\3\26\3\26\3\27\3\27\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0129\n\30\3\30\6\30\u012c\n\30\r\30")
        buf.write("\16\30\u012d\3\31\6\31\u0131\n\31\r\31\16\31\u0132\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u0139\n\32\3\32\6\32\u013c\n\32\r")
        buf.write("\32\16\32\u013d\3\33\3\33\3\33\5\33\u0143\n\33\3\34\3")
        buf.write("\34\3\35\3\35\5\35\u0149\n\35\3\36\3\36\7\36\u014d\n\36")
        buf.write("\f\36\16\36\u0150\13\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3=\3=\3>\3>")
        buf.write("\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3D\3")
        buf.write("E\3E\3E\3F\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3I\3J\3")
        buf.write("J\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3")
        buf.write("R\3S\3S\3T\3T\4\u00cf\u00dd\2U\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2")
        buf.write("%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\13\67\f9\r;\16=\17?\20")
        buf.write("A\21C\22E\23G\24I\25K\26M\27O\30Q\31S\32U\33W\34Y\35[")
        buf.write("\36]\37_ a!c\"e#g$i%k&m\'o(q)s*u+w,y-{.}/\177\60\u0081")
        buf.write("\61\u0083\62\u0085\63\u0087\64\u0089\65\u008b\66\u008d")
        buf.write("\67\u008f8\u00919\u0093:\u0095;\u0097<\u0099=\u009b>\u009d")
        buf.write("?\u009f@\u00a1A\u00a3B\u00a5C\u00a7D\3\2\17\4\3\n\f\16")
        buf.write("\17\4\2\60\60AA\5\2\13\f\16\17\"\"\3\2c|\3\2C\\\3\2\62")
        buf.write(";\4\2--//\4\2GGgg\3\2\60\60\t\2))^^ddhhppttvv\7\2\n\f")
        buf.write("\16\17$$))^^\5\2\62;CHch\3\2\629\2\u0230\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\3\u00a9\3\2\2\2\5\u00ac\3\2\2\2\7\u00b4")
        buf.write("\3\2\2\2\t\u00bd\3\2\2\2\13\u00c9\3\2\2\2\r\u00d7\3\2")
        buf.write("\2\2\17\u00e2\3\2\2\2\21\u00e5\3\2\2\2\23\u00eb\3\2\2")
        buf.write("\2\25\u00ed\3\2\2\2\27\u00ef\3\2\2\2\31\u00f3\3\2\2\2")
        buf.write("\33\u00f6\3\2\2\2\35\u00f8\3\2\2\2\37\u00ff\3\2\2\2!\u0107")
        buf.write("\3\2\2\2#\u0112\3\2\2\2%\u0115\3\2\2\2\'\u0118\3\2\2\2")
        buf.write(")\u011e\3\2\2\2+\u0120\3\2\2\2-\u0122\3\2\2\2/\u0128\3")
        buf.write("\2\2\2\61\u0130\3\2\2\2\63\u0138\3\2\2\2\65\u0142\3\2")
        buf.write("\2\2\67\u0144\3\2\2\29\u0148\3\2\2\2;\u014a\3\2\2\2=\u0154")
        buf.write("\3\2\2\2?\u0159\3\2\2\2A\u015f\3\2\2\2C\u0168\3\2\2\2")
        buf.write("E\u016b\3\2\2\2G\u0170\3\2\2\2I\u0177\3\2\2\2K\u017e\3")
        buf.write("\2\2\2M\u0184\3\2\2\2O\u018b\3\2\2\2Q\u0194\3\2\2\2S\u0198")
        buf.write("\3\2\2\2U\u01a1\3\2\2\2W\u01a4\3\2\2\2Y\u01ae\3\2\2\2")
        buf.write("[\u01b5\3\2\2\2]\u01ba\3\2\2\2_\u01be\3\2\2\2a\u01c4\3")
        buf.write("\2\2\2c\u01c9\3\2\2\2e\u01cf\3\2\2\2g\u01d5\3\2\2\2i\u01d7")
        buf.write("\3\2\2\2k\u01da\3\2\2\2m\u01dc\3\2\2\2o\u01df\3\2\2\2")
        buf.write("q\u01e1\3\2\2\2s\u01e4\3\2\2\2u\u01e6\3\2\2\2w\u01e9\3")
        buf.write("\2\2\2y\u01eb\3\2\2\2{\u01ed\3\2\2\2}\u01f0\3\2\2\2\177")
        buf.write("\u01f3\3\2\2\2\u0081\u01f6\3\2\2\2\u0083\u01f9\3\2\2\2")
        buf.write("\u0085\u01fb\3\2\2\2\u0087\u01fd\3\2\2\2\u0089\u0200\3")
        buf.write("\2\2\2\u008b\u0203\3\2\2\2\u008d\u0207\3\2\2\2\u008f\u020a")
        buf.write("\3\2\2\2\u0091\u020d\3\2\2\2\u0093\u0211\3\2\2\2\u0095")
        buf.write("\u0215\3\2\2\2\u0097\u0217\3\2\2\2\u0099\u0219\3\2\2\2")
        buf.write("\u009b\u021b\3\2\2\2\u009d\u021d\3\2\2\2\u009f\u021f\3")
        buf.write("\2\2\2\u00a1\u0221\3\2\2\2\u00a3\u0223\3\2\2\2\u00a5\u0225")
        buf.write("\3\2\2\2\u00a7\u0227\3\2\2\2\u00a9\u00aa\5\33\16\2\u00aa")
        buf.write("\u00ab\5!\21\2\u00ab\4\3\2\2\2\u00ac\u00b1\5\23\n\2\u00ad")
        buf.write("\u00b0\5\23\n\2\u00ae\u00b0\5\27\f\2\u00af\u00ad\3\2\2")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\6\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\u00b8\7$\2\2\u00b5\u00b7\5)\25\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00bb\u00bc\5#\22\2\u00bc\b\3\2\2\2\u00bd\u00c1")
        buf.write("\7$\2\2\u00be\u00c0\5)\25\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6\t")
        buf.write("\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8")
        buf.write("\b\5\2\2\u00c8\n\3\2\2\2\u00c9\u00ca\7,\2\2\u00ca\u00cb")
        buf.write("\7,\2\2\u00cb\u00cf\3\2\2\2\u00cc\u00ce\13\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d3\7,\2\2\u00d3\u00d4\7,\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d6\b\6\3\2\u00d6\f\3\2\2\2\u00d7\u00d8")
        buf.write("\7,\2\2\u00d8\u00d9\7,\2\2\u00d9\u00dd\3\2\2\2\u00da\u00dc")
        buf.write("\13\2\2\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0\3\2\2\2")
        buf.write("\u00df\u00dd\3\2\2\2\u00e0\u00e1\7\2\2\3\u00e1\16\3\2")
        buf.write("\2\2\u00e2\u00e3\t\3\2\2\u00e3\20\3\2\2\2\u00e4\u00e6")
        buf.write("\t\4\2\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\u00ea\b\t\3\2\u00ea\22\3\2\2\2\u00eb\u00ec\t\5")
        buf.write("\2\2\u00ec\24\3\2\2\2\u00ed\u00ee\t\6\2\2\u00ee\26\3\2")
        buf.write("\2\2\u00ef\u00f0\t\7\2\2\u00f0\30\3\2\2\2\u00f1\u00f4")
        buf.write("\5\23\n\2\u00f2\u00f4\5\25\13\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\32\3\2\2\2\u00f5\u00f7\t\b\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\34\3\2\2\2\u00f8")
        buf.write("\u00f9\t\t\2\2\u00f9\u00fb\5\33\16\2\u00fa\u00fc\5\27")
        buf.write("\f\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\36\3\2\2\2\u00ff\u0103")
        buf.write("\t\n\2\2\u0100\u0102\5\27\f\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104 \3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108\5\27\f")
        buf.write("\2\u0107\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u0107")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0110\3\2\2\2\u010b")
        buf.write("\u010d\5\37\20\2\u010c\u010e\5\35\17\2\u010d\u010c\3\2")
        buf.write("\2\2\u010d\u010e\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u0111")
        buf.write("\5\35\17\2\u0110\u010b\3\2\2\2\u0110\u010f\3\2\2\2\u0111")
        buf.write("\"\3\2\2\2\u0112\u0113\7^\2\2\u0113\u0114\n\13\2\2\u0114")
        buf.write("$\3\2\2\2\u0115\u0116\7^\2\2\u0116\u0117\t\13\2\2\u0117")
        buf.write("&\3\2\2\2\u0118\u0119\7)\2\2\u0119\u011a\7$\2\2\u011a")
        buf.write("(\3\2\2\2\u011b\u011f\n\f\2\2\u011c\u011f\5%\23\2\u011d")
        buf.write("\u011f\5\'\24\2\u011e\u011b\3\2\2\2\u011e\u011c\3\2\2")
        buf.write("\2\u011e\u011d\3\2\2\2\u011f*\3\2\2\2\u0120\u0121\t\r")
        buf.write("\2\2\u0121,\3\2\2\2\u0122\u0123\t\16\2\2\u0123.\3\2\2")
        buf.write("\2\u0124\u0125\7\62\2\2\u0125\u0129\7z\2\2\u0126\u0127")
        buf.write("\7\62\2\2\u0127\u0129\7Z\2\2\u0128\u0124\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u012c\5+\26\2")
        buf.write("\u012b\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3")
        buf.write("\2\2\2\u012d\u012e\3\2\2\2\u012e\60\3\2\2\2\u012f\u0131")
        buf.write("\5\27\f\2\u0130\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132")
        buf.write("\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\62\3\2\2\2\u0134")
        buf.write("\u0135\7\62\2\2\u0135\u0139\7q\2\2\u0136\u0137\7\62\2")
        buf.write("\2\u0137\u0139\7Q\2\2\u0138\u0134\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u013c\5-\27\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\64\3\2\2\2\u013f\u0143\5\61")
        buf.write("\31\2\u0140\u0143\5/\30\2\u0141\u0143\5\63\32\2\u0142")
        buf.write("\u013f\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143\66\3\2\2\2\u0144\u0145\5!\21\2\u01458\3\2\2\2\u0146")
        buf.write("\u0149\5a\61\2\u0147\u0149\5c\62\2\u0148\u0146\3\2\2\2")
        buf.write("\u0148\u0147\3\2\2\2\u0149:\3\2\2\2\u014a\u014e\7$\2\2")
        buf.write("\u014b\u014d\5)\25\2\u014c\u014b\3\2\2\2\u014d\u0150\3")
        buf.write("\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\7$\2\2\u0152")
        buf.write("\u0153\b\36\4\2\u0153<\3\2\2\2\u0154\u0155\7D\2\2\u0155")
        buf.write("\u0156\7q\2\2\u0156\u0157\7f\2\2\u0157\u0158\7{\2\2\u0158")
        buf.write(">\3\2\2\2\u0159\u015a\7D\2\2\u015a\u015b\7t\2\2\u015b")
        buf.write("\u015c\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e\7m\2\2\u015e")
        buf.write("@\3\2\2\2\u015f\u0160\7E\2\2\u0160\u0161\7q\2\2\u0161")
        buf.write("\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164\7k\2\2\u0164")
        buf.write("\u0165\7p\2\2\u0165\u0166\7w\2\2\u0166\u0167\7g\2\2\u0167")
        buf.write("B\3\2\2\2\u0168\u0169\7F\2\2\u0169\u016a\7q\2\2\u016a")
        buf.write("D\3\2\2\2\u016b\u016c\7G\2\2\u016c\u016d\7n\2\2\u016d")
        buf.write("\u016e\7u\2\2\u016e\u016f\7g\2\2\u016fF\3\2\2\2\u0170")
        buf.write("\u0171\7G\2\2\u0171\u0172\7n\2\2\u0172\u0173\7U\2\2\u0173")
        buf.write("\u0174\7g\2\2\u0174\u0175\7n\2\2\u0175\u0176\7h\2\2\u0176")
        buf.write("H\3\2\2\2\u0177\u0178\7G\2\2\u0178\u0179\7n\2\2\u0179")
        buf.write("\u017a\7u\2\2\u017a\u017b\7g\2\2\u017b\u017c\7K\2\2\u017c")
        buf.write("\u017d\7h\2\2\u017dJ\3\2\2\2\u017e\u017f\7G\2\2\u017f")
        buf.write("\u0180\7p\2\2\u0180\u0181\7f\2\2\u0181\u0182\7K\2\2\u0182")
        buf.write("\u0183\7h\2\2\u0183L\3\2\2\2\u0184\u0185\7G\2\2\u0185")
        buf.write("\u0186\7p\2\2\u0186\u0187\7f\2\2\u0187\u0188\7H\2\2\u0188")
        buf.write("\u0189\7q\2\2\u0189\u018a\7t\2\2\u018aN\3\2\2\2\u018b")
        buf.write("\u018c\7G\2\2\u018c\u018d\7p\2\2\u018d\u018e\7f\2\2\u018e")
        buf.write("\u018f\7Y\2\2\u018f\u0190\7j\2\2\u0190\u0191\7k\2\2\u0191")
        buf.write("\u0192\7n\2\2\u0192\u0193\7g\2\2\u0193P\3\2\2\2\u0194")
        buf.write("\u0195\7H\2\2\u0195\u0196\7q\2\2\u0196\u0197\7t\2\2\u0197")
        buf.write("R\3\2\2\2\u0198\u0199\7H\2\2\u0199\u019a\7w\2\2\u019a")
        buf.write("\u019b\7p\2\2\u019b\u019c\7e\2\2\u019c\u019d\7v\2\2\u019d")
        buf.write("\u019e\7k\2\2\u019e\u019f\7q\2\2\u019f\u01a0\7p\2\2\u01a0")
        buf.write("T\3\2\2\2\u01a1\u01a2\7K\2\2\u01a2\u01a3\7h\2\2\u01a3")
        buf.write("V\3\2\2\2\u01a4\u01a5\7R\2\2\u01a5\u01a6\7c\2\2\u01a6")
        buf.write("\u01a7\7t\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9\7o\2\2\u01a9")
        buf.write("\u01aa\7g\2\2\u01aa\u01ab\7v\2\2\u01ab\u01ac\7g\2\2\u01ac")
        buf.write("\u01ad\7t\2\2\u01adX\3\2\2\2\u01ae\u01af\7T\2\2\u01af")
        buf.write("\u01b0\7g\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7w\2\2\u01b2")
        buf.write("\u01b3\7t\2\2\u01b3\u01b4\7p\2\2\u01b4Z\3\2\2\2\u01b5")
        buf.write("\u01b6\7V\2\2\u01b6\u01b7\7j\2\2\u01b7\u01b8\7g\2\2\u01b8")
        buf.write("\u01b9\7p\2\2\u01b9\\\3\2\2\2\u01ba\u01bb\7X\2\2\u01bb")
        buf.write("\u01bc\7c\2\2\u01bc\u01bd\7t\2\2\u01bd^\3\2\2\2\u01be")
        buf.write("\u01bf\7Y\2\2\u01bf\u01c0\7j\2\2\u01c0\u01c1\7k\2\2\u01c1")
        buf.write("\u01c2\7n\2\2\u01c2\u01c3\7g\2\2\u01c3`\3\2\2\2\u01c4")
        buf.write("\u01c5\7V\2\2\u01c5\u01c6\7t\2\2\u01c6\u01c7\7w\2\2\u01c7")
        buf.write("\u01c8\7g\2\2\u01c8b\3\2\2\2\u01c9\u01ca\7H\2\2\u01ca")
        buf.write("\u01cb\7c\2\2\u01cb\u01cc\7n\2\2\u01cc\u01cd\7u\2\2\u01cd")
        buf.write("\u01ce\7g\2\2\u01ced\3\2\2\2\u01cf\u01d0\7G\2\2\u01d0")
        buf.write("\u01d1\7p\2\2\u01d1\u01d2\7f\2\2\u01d2\u01d3\7F\2\2\u01d3")
        buf.write("\u01d4\7q\2\2\u01d4f\3\2\2\2\u01d5\u01d6\7-\2\2\u01d6")
        buf.write("h\3\2\2\2\u01d7\u01d8\7-\2\2\u01d8\u01d9\7\60\2\2\u01d9")
        buf.write("j\3\2\2\2\u01da\u01db\7/\2\2\u01dbl\3\2\2\2\u01dc\u01dd")
        buf.write("\7/\2\2\u01dd\u01de\7\60\2\2\u01den\3\2\2\2\u01df\u01e0")
        buf.write("\7,\2\2\u01e0p\3\2\2\2\u01e1\u01e2\7,\2\2\u01e2\u01e3")
        buf.write("\7\60\2\2\u01e3r\3\2\2\2\u01e4\u01e5\7^\2\2\u01e5t\3\2")
        buf.write("\2\2\u01e6\u01e7\7^\2\2\u01e7\u01e8\7\60\2\2\u01e8v\3")
        buf.write("\2\2\2\u01e9\u01ea\7\'\2\2\u01eax\3\2\2\2\u01eb\u01ec")
        buf.write("\7#\2\2\u01ecz\3\2\2\2\u01ed\u01ee\7(\2\2\u01ee\u01ef")
        buf.write("\7(\2\2\u01ef|\3\2\2\2\u01f0\u01f1\7~\2\2\u01f1\u01f2")
        buf.write("\7~\2\2\u01f2~\3\2\2\2\u01f3\u01f4\7?\2\2\u01f4\u01f5")
        buf.write("\7?\2\2\u01f5\u0080\3\2\2\2\u01f6\u01f7\7#\2\2\u01f7\u01f8")
        buf.write("\7?\2\2\u01f8\u0082\3\2\2\2\u01f9\u01fa\7>\2\2\u01fa\u0084")
        buf.write("\3\2\2\2\u01fb\u01fc\7@\2\2\u01fc\u0086\3\2\2\2\u01fd")
        buf.write("\u01fe\7>\2\2\u01fe\u01ff\7?\2\2\u01ff\u0088\3\2\2\2\u0200")
        buf.write("\u0201\7@\2\2\u0201\u0202\7?\2\2\u0202\u008a\3\2\2\2\u0203")
        buf.write("\u0204\7?\2\2\u0204\u0205\7^\2\2\u0205\u0206\7?\2\2\u0206")
        buf.write("\u008c\3\2\2\2\u0207\u0208\7>\2\2\u0208\u0209\7\60\2\2")
        buf.write("\u0209\u008e\3\2\2\2\u020a\u020b\7@\2\2\u020b\u020c\7")
        buf.write("\60\2\2\u020c\u0090\3\2\2\2\u020d\u020e\7>\2\2\u020e\u020f")
        buf.write("\7?\2\2\u020f\u0210\7\60\2\2\u0210\u0092\3\2\2\2\u0211")
        buf.write("\u0212\7@\2\2\u0212\u0213\7?\2\2\u0213\u0214\7\60\2\2")
        buf.write("\u0214\u0094\3\2\2\2\u0215\u0216\7*\2\2\u0216\u0096\3")
        buf.write("\2\2\2\u0217\u0218\7+\2\2\u0218\u0098\3\2\2\2\u0219\u021a")
        buf.write("\7]\2\2\u021a\u009a\3\2\2\2\u021b\u021c\7_\2\2\u021c\u009c")
        buf.write("\3\2\2\2\u021d\u021e\7}\2\2\u021e\u009e\3\2\2\2\u021f")
        buf.write("\u0220\7\177\2\2\u0220\u00a0\3\2\2\2\u0221\u0222\7<\2")
        buf.write("\2\u0222\u00a2\3\2\2\2\u0223\u0224\7\60\2\2\u0224\u00a4")
        buf.write("\3\2\2\2\u0225\u0226\7=\2\2\u0226\u00a6\3\2\2\2\u0227")
        buf.write("\u0228\7.\2\2\u0228\u00a8\3\2\2\2\33\2\u00af\u00b1\u00b8")
        buf.write("\u00c1\u00c5\u00cf\u00dd\u00e7\u00f3\u00f6\u00fd\u0103")
        buf.write("\u0109\u010d\u0110\u011e\u0128\u012d\u0132\u0138\u013d")
        buf.write("\u0142\u0148\u014e\5\3\5\2\b\2\2\3\36\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    REAL_NUMBER = 1
    ID = 2
    ILLEGAL_ESCAPE = 3
    UNCLOSE_STRING = 4
    COMMENT = 5
    UNTERMINATED_COMMENT = 6
    ERROR_CHAR = 7
    WS = 8
    Integer_literal = 9
    Float_literal = 10
    Boolean_literal = 11
    String_literal = 12
    BODY = 13
    BREAK = 14
    CONTINUE = 15
    DO = 16
    ELSE = 17
    ELSELF = 18
    ELSEIF = 19
    ENDBODY = 20
    ENDFOR = 21
    ENDWHILE = 22
    FOR = 23
    FUNCTION = 24
    IF = 25
    PARAMETER = 26
    RETURN = 27
    THEN = 28
    VAR = 29
    WHILE = 30
    TRUE = 31
    FALSE = 32
    ENDDO = 33
    PLUS_INT = 34
    PLUS_FLOAT = 35
    MINUS_INT = 36
    MINUS_FLOAT = 37
    STAR_INT = 38
    STAR_FLOAT = 39
    DIV_INT = 40
    DIV_FLOAT = 41
    MOD = 42
    NOT = 43
    AND = 44
    OR = 45
    EQUAL = 46
    NOT_EQUAL_INT = 47
    LESS_INT = 48
    GREATER_INT = 49
    LESS_OR_EQUAL_INT = 50
    GREATER_OR_EQUAL_INT = 51
    NOT_EQUAL_FLOAT = 52
    LESS_FLOAT = 53
    GREATER_FLOAT = 54
    LESS_OR_EQUAL_FLOAT = 55
    GREATER_OR_EQUAL_FLOAT = 56
    LEFT_PAREN = 57
    RIGHT_PARENT = 58
    LEFT_BRACKET = 59
    RIGHT_BRACKET = 60
    LEFT_BRACE = 61
    RIGHT_BRACE = 62
    COLON = 63
    DOT = 64
    SEMI = 65
    COMMA = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElSelf'", 
            "'ElseIf'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", 
            "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=\\='", "'<.'", 
            "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "':'", "'.'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "REAL_NUMBER", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS", "Integer_literal", 
            "Float_literal", "Boolean_literal", "String_literal", "BODY", 
            "BREAK", "CONTINUE", "DO", "ELSE", "ELSELF", "ELSEIF", "ENDBODY", 
            "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", 
            "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", 
            "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", 
            "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
            "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
            "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
            "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA" ]

    ruleNames = [ "REAL_NUMBER", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS", 
                  "LOWERCASE_LETTER", "UPPERCASE_LETTER", "DIGIT", "LETTER", 
                  "SIGN", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
                  "ILL_ESC_SEQUENCE", "SUP_ESC_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", 
                  "STRING_CHAR", "HEXADECIMALDIGIT", "OCTALDIGIT", "HEXADECIMAL", 
                  "DECIMAL", "OCTAL", "Integer_literal", "Float_literal", 
                  "Boolean_literal", "String_literal", "BODY", "BREAK", 
                  "CONTINUE", "DO", "ELSE", "ELSELF", "ELSEIF", "ENDBODY", 
                  "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                  "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
                  "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                  "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", 
                  "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
                  "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                  "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
                  "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PARENT", 
                  "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
                  "COLON", "DOT", "SEMI", "COMMA" ]

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
            actions[3] = self.UNCLOSE_STRING_action 
            actions[28] = self.String_literal_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    y = self.text;
                    self.text = y[1:]
                
     

    def String_literal_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    y = str(self.text)
                    self.text = y[1:-1]
                
     


