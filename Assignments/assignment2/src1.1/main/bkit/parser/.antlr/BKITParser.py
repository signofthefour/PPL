# Generated from /home/nguyendat/Documents/projects/PPL/Assignments/assignment2/src1.1/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S")
        buf.write("\u01ac\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\3\2\3\2\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\7\2")
        buf.write("X\n\2\f\2\16\2[\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4i\n\4\3\4\3\4\3\4\3\4\3\4\7\4p\n\4\f")
        buf.write("\4\16\4s\13\4\3\4\7\4v\n\4\f\4\16\4y\13\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5\u0081\n\5\f\5\16\5\u0084\13\5\3\5\7\5")
        buf.write("\u0087\n\5\f\5\16\5\u008a\13\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\u009f\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00aa")
        buf.write("\n\7\f\7\16\7\u00ad\13\7\3\7\3\7\5\7\u00b1\n\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00d7\n\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\5\20\u00e4")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00eb\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u00f3\n\22\f\22\16\22\u00f6")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00fe\n\23\f")
        buf.write("\23\16\23\u0101\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u0109\n\24\f\24\16\24\u010c\13\24\3\25\3\25\3\25\5")
        buf.write("\25\u0111\n\25\3\26\3\26\3\26\5\26\u0116\n\26\3\27\3\27")
        buf.write("\5\27\u011a\n\27\3\30\3\30\5\30\u011e\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\5\31\u0125\n\31\3\32\3\32\3\32\5\32\u012a")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\33\7\33\u0131\n\33\f\33\16")
        buf.write("\33\u0134\13\33\7\33\u0136\n\33\f\33\16\33\u0139\13\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0146\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3")
        buf.write("\37\3\37\5\37\u0151\n\37\3\37\3\37\3\37\5\37\u0156\n\37")
        buf.write("\7\37\u0158\n\37\f\37\16\37\u015b\13\37\5\37\u015d\n\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \6 \u0166\n \r \16 \u0167\3!")
        buf.write("\3!\5!\u016c\n!\3!\3!\3!\5!\u0171\n!\7!\u0173\n!\f!\16")
        buf.write("!\u0176\13!\3\"\3\"\3\"\3\"\6\"\u017c\n\"\r\"\16\"\u017d")
        buf.write("\3\"\5\"\u0181\n\"\3\"\3\"\3\"\5\"\u0186\n\"\3#\3#\3#")
        buf.write("\3#\6#\u018c\n#\r#\16#\u018d\3#\5#\u0191\n#\3$\3$\3$\3")
        buf.write("$\3$\6$\u0198\n$\r$\16$\u0199\3%\3%\3%\3%\3&\3&\3&\3&")
        buf.write("\3\'\3\'\3\'\7\'\u01a7\n\'\f\'\16\'\u01aa\13\'\3\'\2\5")
        buf.write("\"$&(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.")
        buf.write("\60\62\64\668:<>@BDFHJL\2\3\3\2\n\r\2\u01b5\2S\3\2\2\2")
        buf.write("\4^\3\2\2\2\6b\3\2\2\2\b\u0082\3\2\2\2\n\u009e\3\2\2\2")
        buf.write("\f\u00a0\3\2\2\2\16\u00b5\3\2\2\2\20\u00b7\3\2\2\2\22")
        buf.write("\u00c6\3\2\2\2\24\u00cd\3\2\2\2\26\u00d6\3\2\2\2\30\u00db")
        buf.write("\3\2\2\2\32\u00dd\3\2\2\2\34\u00df\3\2\2\2\36\u00e1\3")
        buf.write("\2\2\2 \u00ea\3\2\2\2\"\u00ec\3\2\2\2$\u00f7\3\2\2\2&")
        buf.write("\u0102\3\2\2\2(\u0110\3\2\2\2*\u0115\3\2\2\2,\u0119\3")
        buf.write("\2\2\2.\u011d\3\2\2\2\60\u0124\3\2\2\2\62\u0129\3\2\2")
        buf.write("\2\64\u012b\3\2\2\2\66\u0145\3\2\2\28\u0147\3\2\2\2:\u014b")
        buf.write("\3\2\2\2<\u014d\3\2\2\2>\u0160\3\2\2\2@\u016b\3\2\2\2")
        buf.write("B\u0180\3\2\2\2D\u0190\3\2\2\2F\u0192\3\2\2\2H\u019b\3")
        buf.write("\2\2\2J\u019f\3\2\2\2L\u01a3\3\2\2\2NO\5\4\3\2OP\7B\2")
        buf.write("\2PR\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T")
        buf.write("Y\3\2\2\2US\3\2\2\2VX\5\6\4\2WV\3\2\2\2X[\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\2\2\3]\3\3")
        buf.write("\2\2\2^_\7\36\2\2_`\7@\2\2`a\5@!\2a\5\3\2\2\2bc\7\31\2")
        buf.write("\2cd\7@\2\2dh\7\3\2\2ef\7\33\2\2fg\7@\2\2gi\5L\'\2he\3")
        buf.write("\2\2\2hi\3\2\2\2ij\3\2\2\2jk\7\16\2\2kq\7@\2\2lm\5\16")
        buf.write("\b\2mn\7B\2\2np\3\2\2\2ol\3\2\2\2ps\3\2\2\2qo\3\2\2\2")
        buf.write("qr\3\2\2\2rw\3\2\2\2sq\3\2\2\2tv\5\n\6\2ut\3\2\2\2vy\3")
        buf.write("\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\7\25")
        buf.write("\2\2{|\7A\2\2|\7\3\2\2\2}~\5\16\b\2~\177\7B\2\2\177\u0081")
        buf.write("\3\2\2\2\u0080}\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0088\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0085\u0087\5\n\6\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3")
        buf.write("\2\2\2\u0089\t\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u009f")
        buf.write("\5\f\7\2\u008c\u009f\5\20\t\2\u008d\u009f\5\22\n\2\u008e")
        buf.write("\u009f\5\24\13\2\u008f\u0090\5\26\f\2\u0090\u0091\7B\2")
        buf.write("\2\u0091\u009f\3\2\2\2\u0092\u0093\5\30\r\2\u0093\u0094")
        buf.write("\7B\2\2\u0094\u009f\3\2\2\2\u0095\u0096\5\32\16\2\u0096")
        buf.write("\u0097\7B\2\2\u0097\u009f\3\2\2\2\u0098\u0099\5\34\17")
        buf.write("\2\u0099\u009a\7B\2\2\u009a\u009f\3\2\2\2\u009b\u009c")
        buf.write("\5\36\20\2\u009c\u009d\7B\2\2\u009d\u009f\3\2\2\2\u009e")
        buf.write("\u008b\3\2\2\2\u009e\u008c\3\2\2\2\u009e\u008d\3\2\2\2")
        buf.write("\u009e\u008e\3\2\2\2\u009e\u008f\3\2\2\2\u009e\u0092\3")
        buf.write("\2\2\2\u009e\u0095\3\2\2\2\u009e\u0098\3\2\2\2\u009e\u009b")
        buf.write("\3\2\2\2\u009f\13\3\2\2\2\u00a0\u00a1\7\32\2\2\u00a1\u00a2")
        buf.write("\5 \21\2\u00a2\u00a3\7\35\2\2\u00a3\u00ab\5\b\5\2\u00a4")
        buf.write("\u00a5\7\23\2\2\u00a5\u00a6\5 \21\2\u00a6\u00a7\7\35\2")
        buf.write("\2\u00a7\u00a8\5\b\5\2\u00a8\u00aa\3\2\2\2\u00a9\u00a4")
        buf.write("\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00b0\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\u00af\7\22\2\2\u00af\u00b1\5\b\5\2\u00b0\u00ae")
        buf.write("\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2")
        buf.write("\u00b3\7\24\2\2\u00b3\u00b4\7A\2\2\u00b4\r\3\2\2\2\u00b5")
        buf.write("\u00b6\5\4\3\2\u00b6\17\3\2\2\2\u00b7\u00b8\7\30\2\2\u00b8")
        buf.write("\u00b9\7:\2\2\u00b9\u00ba\7\3\2\2\u00ba\u00bb\7D\2\2\u00bb")
        buf.write("\u00bc\5 \21\2\u00bc\u00bd\7C\2\2\u00bd\u00be\5 \21\2")
        buf.write("\u00be\u00bf\7C\2\2\u00bf\u00c0\5 \21\2\u00c0\u00c1\7")
        buf.write(";\2\2\u00c1\u00c2\7\21\2\2\u00c2\u00c3\5\b\5\2\u00c3\u00c4")
        buf.write("\7\26\2\2\u00c4\u00c5\7A\2\2\u00c5\21\3\2\2\2\u00c6\u00c7")
        buf.write("\7\37\2\2\u00c7\u00c8\5 \21\2\u00c8\u00c9\7\21\2\2\u00c9")
        buf.write("\u00ca\5\b\5\2\u00ca\u00cb\7\27\2\2\u00cb\u00cc\7A\2\2")
        buf.write("\u00cc\23\3\2\2\2\u00cd\u00ce\7\21\2\2\u00ce\u00cf\5\b")
        buf.write("\5\2\u00cf\u00d0\7\37\2\2\u00d0\u00d1\5 \21\2\u00d1\u00d2")
        buf.write("\7\"\2\2\u00d2\u00d3\7A\2\2\u00d3\25\3\2\2\2\u00d4\u00d7")
        buf.write("\5> \2\u00d5\u00d7\7\3\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\7D\2\2\u00d9")
        buf.write("\u00da\5 \21\2\u00da\27\3\2\2\2\u00db\u00dc\7\17\2\2\u00dc")
        buf.write("\31\3\2\2\2\u00dd\u00de\7\20\2\2\u00de\33\3\2\2\2\u00df")
        buf.write("\u00e0\5\64\33\2\u00e0\35\3\2\2\2\u00e1\u00e3\7\34\2\2")
        buf.write("\u00e2\u00e4\5 \21\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3")
        buf.write("\2\2\2\u00e4\37\3\2\2\2\u00e5\u00e6\5\"\22\2\u00e6\u00e7")
        buf.write("\7\4\2\2\u00e7\u00e8\5\"\22\2\u00e8\u00eb\3\2\2\2\u00e9")
        buf.write("\u00eb\5\"\22\2\u00ea\u00e5\3\2\2\2\u00ea\u00e9\3\2\2")
        buf.write("\2\u00eb!\3\2\2\2\u00ec\u00ed\b\22\1\2\u00ed\u00ee\5$")
        buf.write("\23\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0\u00f1")
        buf.write("\7\5\2\2\u00f1\u00f3\5$\23\2\u00f2\u00ef\3\2\2\2\u00f3")
        buf.write("\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5#\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\b\23\1")
        buf.write("\2\u00f8\u00f9\5&\24\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb")
        buf.write("\f\4\2\2\u00fb\u00fc\7\6\2\2\u00fc\u00fe\5&\24\2\u00fd")
        buf.write("\u00fa\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100%\3\2\2\2\u0101\u00ff\3\2\2")
        buf.write("\2\u0102\u0103\b\24\1\2\u0103\u0104\5(\25\2\u0104\u010a")
        buf.write("\3\2\2\2\u0105\u0106\f\4\2\2\u0106\u0107\7\7\2\2\u0107")
        buf.write("\u0109\5(\25\2\u0108\u0105\3\2\2\2\u0109\u010c\3\2\2\2")
        buf.write("\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\'\3\2\2")
        buf.write("\2\u010c\u010a\3\2\2\2\u010d\u010e\7\b\2\2\u010e\u0111")
        buf.write("\5(\25\2\u010f\u0111\5*\26\2\u0110\u010d\3\2\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111)\3\2\2\2\u0112\u0113\7\t\2\2\u0113")
        buf.write("\u0116\5*\26\2\u0114\u0116\5,\27\2\u0115\u0112\3\2\2\2")
        buf.write("\u0115\u0114\3\2\2\2\u0116+\3\2\2\2\u0117\u011a\5> \2")
        buf.write("\u0118\u011a\5.\30\2\u0119\u0117\3\2\2\2\u0119\u0118\3")
        buf.write("\2\2\2\u011a-\3\2\2\2\u011b\u011e\5\64\33\2\u011c\u011e")
        buf.write("\5\60\31\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2\u011e")
        buf.write("/\3\2\2\2\u011f\u0125\5\62\32\2\u0120\u0121\7:\2\2\u0121")
        buf.write("\u0122\5 \21\2\u0122\u0123\7;\2\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u011f\3\2\2\2\u0124\u0120\3\2\2\2\u0125\61\3\2")
        buf.write("\2\2\u0126\u012a\7\3\2\2\u0127\u012a\5:\36\2\u0128\u012a")
        buf.write("\5<\37\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2\u0129")
        buf.write("\u0128\3\2\2\2\u012a\63\3\2\2\2\u012b\u012c\7\3\2\2\u012c")
        buf.write("\u0137\7:\2\2\u012d\u0132\5 \21\2\u012e\u012f\7C\2\2\u012f")
        buf.write("\u0131\5 \21\2\u0130\u012e\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0136\3")
        buf.write("\2\2\2\u0134\u0132\3\2\2\2\u0135\u012d\3\2\2\2\u0136\u0139")
        buf.write("\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u013a\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b\7;\2\2")
        buf.write("\u013b\65\3\2\2\2\u013c\u013d\7<\2\2\u013d\u013e\5 \21")
        buf.write("\2\u013e\u013f\7=\2\2\u013f\u0146\3\2\2\2\u0140\u0141")
        buf.write("\7<\2\2\u0141\u0142\5 \21\2\u0142\u0143\7=\2\2\u0143\u0144")
        buf.write("\5\66\34\2\u0144\u0146\3\2\2\2\u0145\u013c\3\2\2\2\u0145")
        buf.write("\u0140\3\2\2\2\u0146\67\3\2\2\2\u0147\u0148\7\3\2\2\u0148")
        buf.write("\u0149\7D\2\2\u0149\u014a\5<\37\2\u014a9\3\2\2\2\u014b")
        buf.write("\u014c\t\2\2\2\u014c;\3\2\2\2\u014d\u015c\7>\2\2\u014e")
        buf.write("\u0151\5:\36\2\u014f\u0151\5<\37\2\u0150\u014e\3\2\2\2")
        buf.write("\u0150\u014f\3\2\2\2\u0151\u0159\3\2\2\2\u0152\u0155\7")
        buf.write("C\2\2\u0153\u0156\5:\36\2\u0154\u0156\5<\37\2\u0155\u0153")
        buf.write("\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0158\3\2\2\2\u0157")
        buf.write("\u0152\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3")
        buf.write("\2\2\2\u015c\u0150\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015e\u015f\7?\2\2\u015f=\3\2\2\2\u0160\u0165")
        buf.write("\5.\30\2\u0161\u0162\7<\2\2\u0162\u0163\5 \21\2\u0163")
        buf.write("\u0164\7=\2\2\u0164\u0166\3\2\2\2\u0165\u0161\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3")
        buf.write("\2\2\2\u0168?\3\2\2\2\u0169\u016c\5D#\2\u016a\u016c\5")
        buf.write("B\"\2\u016b\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\u0174")
        buf.write("\3\2\2\2\u016d\u0170\7C\2\2\u016e\u0171\5D#\2\u016f\u0171")
        buf.write("\5B\"\2\u0170\u016e\3\2\2\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("\u0173\3\2\2\2\u0172\u016d\3\2\2\2\u0173\u0176\3\2\2\2")
        buf.write("\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175A\3\2\2")
        buf.write("\2\u0176\u0174\3\2\2\2\u0177\u017b\7\3\2\2\u0178\u0179")
        buf.write("\7<\2\2\u0179\u017a\7\n\2\2\u017a\u017c\7=\2\2\u017b\u0178")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u0181\7\3\2\2")
        buf.write("\u0180\u0177\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0182\3")
        buf.write("\2\2\2\u0182\u0185\7D\2\2\u0183\u0186\5<\37\2\u0184\u0186")
        buf.write("\5:\36\2\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186")
        buf.write("C\3\2\2\2\u0187\u018b\7\3\2\2\u0188\u0189\7<\2\2\u0189")
        buf.write("\u018a\7\n\2\2\u018a\u018c\7=\2\2\u018b\u0188\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u0191\3\2\2\2\u018f\u0191\7\3\2\2\u0190\u0187")
        buf.write("\3\2\2\2\u0190\u018f\3\2\2\2\u0191E\3\2\2\2\u0192\u0197")
        buf.write("\7\3\2\2\u0193\u0194\7<\2\2\u0194\u0195\5 \21\2\u0195")
        buf.write("\u0196\7=\2\2\u0196\u0198\3\2\2\2\u0197\u0193\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3")
        buf.write("\2\2\2\u019aG\3\2\2\2\u019b\u019c\5F$\2\u019c\u019d\7")
        buf.write("D\2\2\u019d\u019e\5<\37\2\u019eI\3\2\2\2\u019f\u01a0\7")
        buf.write("\3\2\2\u01a0\u01a1\7D\2\2\u01a1\u01a2\5:\36\2\u01a2K\3")
        buf.write("\2\2\2\u01a3\u01a8\5D#\2\u01a4\u01a5\7C\2\2\u01a5\u01a7")
        buf.write("\5D#\2\u01a6\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9M\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2*SYhqw\u0082\u0088\u009e\u00ab\u00b0\u00d6\u00e3")
        buf.write("\u00ea\u00f4\u00ff\u010a\u0110\u0115\u0119\u011d\u0124")
        buf.write("\u0129\u0132\u0137\u0145\u0150\u0155\u0159\u015c\u0167")
        buf.write("\u016b\u0170\u0174\u017d\u0180\u0185\u018d\u0190\u0199")
        buf.write("\u01a8")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
                     "'ElseIf'", "'EndIf'", "'EndBody'", "'EndFor'", "'EndWhile'", 
                     "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", 
                     "'Then'", "'Var'", "'While'", "'True'", "'False'", 
                     "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
                     "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "':'", "'.'", "';'", "','", "'='", "'\"'", 
                     "'int_of_float'", "'int_of_string'", "'float_to_int'", 
                     "'float_of_string'", "'bool_of_string'", "'string_of_bool'", 
                     "'string_of_int'", "'string_of_float'" ]

    symbolicNames = [ "<INVALID>", "ID", "REL_OP", "BIN_LOGICAL_OP", "ADD_OP", 
                      "MUL_OP", "UN_LOGICAL_OP", "UN_OP", "INT_LIT", "FLOAT_LIT", 
                      "BOOL_LIT", "STRING_LIT", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
                      "STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", 
                      "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", 
                      "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
                      "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
                      "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
                      "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", 
                      "DOUBLE_QUOTE", "INT_OF_FLOAT", "INT_OF_STRING", "FLOAT_TO_INT", 
                      "FLOAT_OF_STRING", "BOOL_OF_STRING", "STRING_OF_BOOL", 
                      "STRING_OF_INT", "STRING_OF_FLOAT", "COMMENT", "WS", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_var_declare = 1
    RULE_function_declare = 2
    RULE_stmt_list = 3
    RULE_stmt = 4
    RULE_if_stmt = 5
    RULE_var_declare_stmt = 6
    RULE_for_stmt = 7
    RULE_while_stmt = 8
    RULE_dowhile_stmt = 9
    RULE_assign_stmt = 10
    RULE_break_stmt = 11
    RULE_continue_stmt = 12
    RULE_call_stmt = 13
    RULE_return_stmt = 14
    RULE_expr = 15
    RULE_expr1 = 16
    RULE_expr2 = 17
    RULE_expr3 = 18
    RULE_expr4 = 19
    RULE_expr5 = 20
    RULE_expr6 = 21
    RULE_expr7 = 22
    RULE_expr8 = 23
    RULE_operand = 24
    RULE_function_call = 25
    RULE_index_op = 26
    RULE_array = 27
    RULE_primitive_data = 28
    RULE_array_lit = 29
    RULE_array_cell = 30
    RULE_var_list = 31
    RULE_var_init = 32
    RULE_var_non_init = 33
    RULE_composite_var = 34
    RULE_composite_init = 35
    RULE_primitive_init = 36
    RULE_params_list = 37

    ruleNames =  [ "program", "var_declare", "function_declare", "stmt_list", 
                   "stmt", "if_stmt", "var_declare_stmt", "for_stmt", "while_stmt", 
                   "dowhile_stmt", "assign_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "operand", "function_call", "index_op", "array", "primitive_data", 
                   "array_lit", "array_cell", "var_list", "var_init", "var_non_init", 
                   "composite_var", "composite_init", "primitive_init", 
                   "params_list" ]

    EOF = Token.EOF
    ID=1
    REL_OP=2
    BIN_LOGICAL_OP=3
    ADD_OP=4
    MUL_OP=5
    UN_LOGICAL_OP=6
    UN_OP=7
    INT_LIT=8
    FLOAT_LIT=9
    BOOL_LIT=10
    STRING_LIT=11
    BODY=12
    BREAK=13
    CONTINUE=14
    DO=15
    ELSE=16
    ELSEIF=17
    ENDIF=18
    ENDBODY=19
    ENDFOR=20
    ENDWHILE=21
    FOR=22
    FUNCTION=23
    IF=24
    PARAMETER=25
    RETURN=26
    THEN=27
    VAR=28
    WHILE=29
    TRUE=30
    FALSE=31
    ENDDO=32
    PLUS_INT=33
    PLUS_FLOAT=34
    MINUS_INT=35
    MINUS_FLOAT=36
    STAR_INT=37
    STAR_FLOAT=38
    DIV_INT=39
    DIV_FLOAT=40
    MOD=41
    NOT=42
    AND=43
    OR=44
    EQUAL=45
    NOT_EQUAL_INT=46
    LESS_INT=47
    GREATER_INT=48
    LESS_OR_EQUAL_INT=49
    GREATER_OR_EQUAL_INT=50
    NOT_EQUAL_FLOAT=51
    LESS_FLOAT=52
    GREATER_FLOAT=53
    LESS_OR_EQUAL_FLOAT=54
    GREATER_OR_EQUAL_FLOAT=55
    LEFT_PAREN=56
    RIGHT_PAREN=57
    LEFT_BRACKET=58
    RIGHT_BRACKET=59
    LEFT_BRACE=60
    RIGHT_BRACE=61
    COLON=62
    DOT=63
    SEMI=64
    COMMA=65
    ASSIGN=66
    DOUBLE_QUOTE=67
    INT_OF_FLOAT=68
    INT_OF_STRING=69
    FLOAT_TO_INT=70
    FLOAT_OF_STRING=71
    BOOL_OF_STRING=72
    STRING_OF_BOOL=73
    STRING_OF_INT=74
    STRING_OF_FLOAT=75
    COMMENT=76
    WS=77
    ILLEGAL_ESCAPE=78
    UNCLOSE_STRING=79
    UNTERMINATED_COMMENT=80
    ERROR_CHAR=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declareContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def function_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Function_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Function_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 76
                self.var_declare()
                self.state = 77
                self.match(BKITParser.SEMI)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 84
                self.function_declare()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(BKITParser.VAR)
            self.state = 93
            self.match(BKITParser.COLON)
            self.state = 94
            self.var_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def params_list(self):
            return self.getTypedRuleContext(BKITParser.Params_listContext,0)


        def var_declare_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declare_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_function_declare




    def function_declare(self):

        localctx = BKITParser.Function_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKITParser.FUNCTION)
            self.state = 97
            self.match(BKITParser.COLON)
            self.state = 98
            self.match(BKITParser.ID)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 99
                self.match(BKITParser.PARAMETER)
                self.state = 100
                self.match(BKITParser.COLON)
                self.state = 101
                self.params_list()


            self.state = 104
            self.match(BKITParser.BODY)
            self.state = 105
            self.match(BKITParser.COLON)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 106
                self.var_declare_stmt()
                self.state = 107
                self.match(BKITParser.SEMI)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.DO) | (1 << BKITParser.FOR) | (1 << BKITParser.IF) | (1 << BKITParser.RETURN) | (1 << BKITParser.WHILE) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 114
                self.stmt()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(BKITParser.ENDBODY)
            self.state = 121
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declare_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SEMI)
            else:
                return self.getToken(BKITParser.SEMI, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 123
                self.var_declare_stmt()
                self.state = 124
                self.match(BKITParser.SEMI)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self.stmt() 
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.Dowhile_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.if_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.while_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.dowhile_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.assign_stmt()
                self.state = 142
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.break_stmt()
                self.state = 145
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.continue_stmt()
                self.state = 148
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 150
                self.call_stmt()
                self.state = 151
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 153
                self.return_stmt()
                self.state = 154
                self.match(BKITParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(BKITParser.IF)
            self.state = 159
            self.expr()
            self.state = 160
            self.match(BKITParser.THEN)
            self.state = 161
            self.stmt_list()
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 162
                self.match(BKITParser.ELSEIF)
                self.state = 163
                self.expr()
                self.state = 164
                self.match(BKITParser.THEN)
                self.state = 165
                self.stmt_list()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 172
                self.match(BKITParser.ELSE)
                self.state = 173
                self.stmt_list()


            self.state = 176
            self.match(BKITParser.ENDIF)
            self.state = 177
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare_stmt




    def var_declare_stmt(self):

        localctx = BKITParser.Var_declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_declare_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.var_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BKITParser.FOR)
            self.state = 182
            self.match(BKITParser.LEFT_PAREN)
            self.state = 183
            self.match(BKITParser.ID)
            self.state = 184
            self.match(BKITParser.ASSIGN)
            self.state = 185
            self.expr()
            self.state = 186
            self.match(BKITParser.COMMA)
            self.state = 187
            self.expr()
            self.state = 188
            self.match(BKITParser.COMMA)
            self.state = 189
            self.expr()
            self.state = 190
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 191
            self.match(BKITParser.DO)
            self.state = 192
            self.stmt_list()
            self.state = 193
            self.match(BKITParser.ENDFOR)
            self.state = 194
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(BKITParser.WHILE)
            self.state = 197
            self.expr()
            self.state = 198
            self.match(BKITParser.DO)
            self.state = 199
            self.stmt_list()
            self.state = 200
            self.match(BKITParser.ENDWHILE)
            self.state = 201
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dowhile_stmt




    def dowhile_stmt(self):

        localctx = BKITParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BKITParser.DO)
            self.state = 204
            self.stmt_list()
            self.state = 205
            self.match(BKITParser.WHILE)
            self.state = 206
            self.expr()
            self.state = 207
            self.match(BKITParser.ENDDO)
            self.state = 208
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def array_cell(self):
            return self.getTypedRuleContext(BKITParser.Array_cellContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 210
                self.array_cell()
                pass

            elif la_ == 2:
                self.state = 211
                self.match(BKITParser.ID)
                pass


            self.state = 214
            self.match(BKITParser.ASSIGN)
            self.state = 215
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(BKITParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(BKITParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.function_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BKITParser.RETURN)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.UN_LOGICAL_OP) | (1 << BKITParser.UN_OP) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 224
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Expr1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Expr1Context,i)


        def REL_OP(self):
            return self.getToken(BKITParser.REL_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr




    def expr(self):

        localctx = BKITParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.expr1(0)
                self.state = 228
                self.match(BKITParser.REL_OP)
                self.state = 229
                self.expr1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(BKITParser.Expr1Context,0)


        def BIN_LOGICAL_OP(self):
            return self.getToken(BKITParser.BIN_LOGICAL_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    self.match(BKITParser.BIN_LOGICAL_OP)
                    self.state = 239
                    self.expr2(0) 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(BKITParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(BKITParser.Expr2Context,0)


        def ADD_OP(self):
            return self.getToken(BKITParser.ADD_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 248
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 249
                    self.match(BKITParser.ADD_OP)
                    self.state = 250
                    self.expr3(0) 
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(BKITParser.Expr3Context,0)


        def MUL_OP(self):
            return self.getToken(BKITParser.MUL_OP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 259
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 260
                    self.match(BKITParser.MUL_OP)
                    self.state = 261
                    self.expr4() 
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UN_LOGICAL_OP(self):
            return self.getToken(BKITParser.UN_LOGICAL_OP, 0)

        def expr4(self):
            return self.getTypedRuleContext(BKITParser.Expr4Context,0)


        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr4




    def expr4(self):

        localctx = BKITParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr4)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.UN_LOGICAL_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(BKITParser.UN_LOGICAL_OP)
                self.state = 268
                self.expr4()
                pass
            elif token in [BKITParser.ID, BKITParser.UN_OP, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.expr5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UN_OP(self):
            return self.getToken(BKITParser.UN_OP, 0)

        def expr5(self):
            return self.getTypedRuleContext(BKITParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(BKITParser.Expr6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr5




    def expr5(self):

        localctx = BKITParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr5)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.UN_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(BKITParser.UN_OP)
                self.state = 273
                self.expr5()
                pass
            elif token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_cell(self):
            return self.getTypedRuleContext(BKITParser.Array_cellContext,0)


        def expr7(self):
            return self.getTypedRuleContext(BKITParser.Expr7Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr6




    def expr6(self):

        localctx = BKITParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.array_cell()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.expr7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def expr8(self):
            return self.getTypedRuleContext(BKITParser.Expr8Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr7




    def expr7(self):

        localctx = BKITParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr7)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.expr8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_expr8




    def expr8(self):

        localctx = BKITParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr8)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID, BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.operand()
                pass
            elif token in [BKITParser.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(BKITParser.LEFT_PAREN)
                self.state = 287
                self.expr()
                self.state = 288
                self.match(BKITParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operand)
        try:
            self.state = 295
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(BKITParser.ID)
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.primitive_data()
                pass
            elif token in [BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 294
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_function_call




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BKITParser.ID)
            self.state = 298
            self.match(BKITParser.LEFT_PAREN)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.UN_LOGICAL_OP) | (1 << BKITParser.UN_OP) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 299
                self.expr()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 300
                    self.match(BKITParser.COMMA)
                    self.state = 301
                    self.expr()
                    self.state = 306
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(BKITParser.ExprContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKITParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_op




    def index_op(self):

        localctx = BKITParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_index_op)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 315
                self.expr()
                self.state = 316
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 319
                self.expr()
                self.state = 320
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 321
                self.index_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(BKITParser.ID)
            self.state = 326
            self.match(BKITParser.ASSIGN)
            self.state = 327
            self.array_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_dataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_data




    def primitive_data(self):

        localctx = BKITParser.Primitive_dataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primitive_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(BKITParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(BKITParser.RIGHT_BRACE, 0)

        def primitive_data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Primitive_dataContext)
            else:
                return self.getTypedRuleContext(BKITParser.Primitive_dataContext,i)


        def array_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Array_litContext)
            else:
                return self.getTypedRuleContext(BKITParser.Array_litContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_lit




    def array_lit(self):

        localctx = BKITParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(BKITParser.LEFT_BRACE)
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LEFT_BRACE))) != 0):
                self.state = 334
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                    self.state = 332
                    self.primitive_data()
                    pass
                elif token in [BKITParser.LEFT_BRACE]:
                    self.state = 333
                    self.array_lit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 336
                    self.match(BKITParser.COMMA)
                    self.state = 339
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                        self.state = 337
                        self.primitive_data()
                        pass
                    elif token in [BKITParser.LEFT_BRACE]:
                        self.state = 338
                        self.array_lit()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 345
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 348
            self.match(BKITParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_cellContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(BKITParser.Expr7Context,0)


        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_cell




    def array_cell(self):

        localctx = BKITParser.Array_cellContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_array_cell)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.expr7()
            self.state = 355 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 351
                    self.match(BKITParser.LEFT_BRACKET)
                    self.state = 352
                    self.expr()
                    self.state = 353
                    self.match(BKITParser.RIGHT_BRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 357 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_non_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_non_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_non_initContext,i)


        def var_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_list




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 359
                self.var_non_init()
                pass

            elif la_ == 2:
                self.state = 360
                self.var_init()
                pass


            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 363
                self.match(BKITParser.COMMA)
                self.state = 366
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 364
                    self.var_non_init()
                    pass

                elif la_ == 2:
                    self.state = 365
                    self.var_init()
                    pass


                self.state = 372
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_init




    def var_init(self):

        localctx = BKITParser.Var_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_var_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 373
                self.match(BKITParser.ID)
                self.state = 377 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 374
                    self.match(BKITParser.LEFT_BRACKET)
                    self.state = 375
                    self.match(BKITParser.INT_LIT)
                    self.state = 376
                    self.match(BKITParser.RIGHT_BRACKET)
                    self.state = 379 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKITParser.LEFT_BRACKET):
                        break

                pass

            elif la_ == 2:
                self.state = 381
                self.match(BKITParser.ID)
                pass


            self.state = 384
            self.match(BKITParser.ASSIGN)
            self.state = 387
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_BRACE]:
                self.state = 385
                self.array_lit()
                pass
            elif token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.state = 386
                self.primitive_data()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_non_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_non_init




    def var_non_init(self):

        localctx = BKITParser.Var_non_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_var_non_init)
        self._la = 0 # Token type
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(BKITParser.ID)
                self.state = 393 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 390
                    self.match(BKITParser.LEFT_BRACKET)
                    self.state = 391
                    self.match(BKITParser.INT_LIT)
                    self.state = 392
                    self.match(BKITParser.RIGHT_BRACKET)
                    self.state = 395 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKITParser.LEFT_BRACKET):
                        break

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LEFT_BRACKET)
            else:
                return self.getToken(BKITParser.LEFT_BRACKET, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExprContext,i)


        def RIGHT_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RIGHT_BRACKET)
            else:
                return self.getToken(BKITParser.RIGHT_BRACKET, i)

        def getRuleIndex(self):
            return BKITParser.RULE_composite_var




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(BKITParser.ID)
            self.state = 405 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 401
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 402
                self.expr()
                self.state = 403
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 407 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LEFT_BRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKITParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_composite_init




    def composite_init(self):

        localctx = BKITParser.Composite_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_composite_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.composite_var()
            self.state = 410
            self.match(BKITParser.ASSIGN)
            self.state = 411
            self.array_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def primitive_data(self):
            return self.getTypedRuleContext(BKITParser.Primitive_dataContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_primitive_init




    def primitive_init(self):

        localctx = BKITParser.Primitive_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_primitive_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(BKITParser.ID)
            self.state = 414
            self.match(BKITParser.ASSIGN)
            self.state = 415
            self.primitive_data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Params_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_non_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_non_initContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_non_initContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_params_list




    def params_list(self):

        localctx = BKITParser.Params_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_params_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.var_non_init()
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 418
                self.match(BKITParser.COMMA)
                self.state = 419
                self.var_non_init()
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr1_sempred
        self._predicates[17] = self.expr2_sempred
        self._predicates[18] = self.expr3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




