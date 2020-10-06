// Generated from /home/nguyendat/Documents/projects/PPL/SyntaxAnalysis/tut/src/forJava/BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		Integer_literal=1, Float_literal=2, String_literal=3, RETURN=4, INT=5, 
		FLOAT=6, PLUS_INT=7, MINUS_INT=8, STAR_INT=9, DIV_INT=10, LEFT_PAREN=11, 
		RIGHT_PAREN=12, LEFT_BRACKET=13, RIGHT_BRACKET=14, LEFT_BRACE=15, RIGHT_BRACE=16, 
		COLON=17, DOT=18, SEMI=19, COMMA=20, ASSIGN=21, ID=22, ILLEGAL_ESCAPE=23, 
		UNCLOSE_STRING=24, COMMENT=25, UNTERMINATED_COMMENT=26, ERROR_CHAR=27, 
		WS=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LOWERCASE_LETTER", "UPPERCASE_LETTER", "DIGIT", "LETTER", "SCIENTIFIC", 
			"DECIMAL_POINT", "FLOATING_POINT_NUM", "ILL_ESC_SEQUENCE", "SUP_ESC_SEQUENCE", 
			"DOUBLE_QUOTE_IN_STRING", "STRING_CHAR", "HEXADECIMALDIGIT", "OCTALDIGIT", 
			"HEXADECIMAL", "DECIMAL", "OCTAL", "Integer_literal", "Float_literal", 
			"String_literal", "RETURN", "INT", "FLOAT", "PLUS_INT", "MINUS_INT", 
			"STAR_INT", "DIV_INT", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", 
			"LEFT_BRACE", "RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA", "ASSIGN", 
			"ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
			"ERROR_CHAR", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, "'+'", "'-'", "'*'", "'/'", 
			"'('", "')'", "'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", "','", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "Integer_literal", "Float_literal", "String_literal", "RETURN", 
			"INT", "FLOAT", "PLUS_INT", "MINUS_INT", "STAR_INT", "DIV_INT", "LEFT_PAREN", 
			"RIGHT_PAREN", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", 
			"COLON", "DOT", "SEMI", "COMMA", "ASSIGN", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
			"COMMENT", "UNTERMINATED_COMMENT", "ERROR_CHAR", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public BKITLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36\u0129\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\5\5d\n\5\3\6\3\6\5\6h\n"+
		"\6\3\6\6\6k\n\6\r\6\16\6l\3\7\3\7\7\7q\n\7\f\7\16\7t\13\7\3\b\6\bw\n\b"+
		"\r\b\16\bx\3\b\3\b\5\b}\n\b\3\b\5\b\u0080\n\b\3\t\3\t\3\t\3\n\3\n\3\n"+
		"\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u008e\n\f\3\r\3\r\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\5\17\u0098\n\17\3\17\6\17\u009b\n\17\r\17\16\17\u009c\3\20"+
		"\6\20\u00a0\n\20\r\20\16\20\u00a1\3\21\3\21\3\21\3\21\5\21\u00a8\n\21"+
		"\3\21\6\21\u00ab\n\21\r\21\16\21\u00ac\3\22\3\22\3\22\5\22\u00b2\n\22"+
		"\3\23\3\23\3\24\3\24\7\24\u00b8\n\24\f\24\16\24\u00bb\13\24\3\24\3\24"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35"+
		"\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&"+
		"\3\'\3\'\3\'\7\'\u00f1\n\'\f\'\16\'\u00f4\13\'\3(\3(\7(\u00f8\n(\f(\16"+
		"(\u00fb\13(\3(\3(\3)\3)\7)\u0101\n)\f)\16)\u0104\13)\3)\3)\3*\3*\3*\3"+
		"*\7*\u010c\n*\f*\16*\u010f\13*\3*\3*\3*\3*\3*\3+\3+\3+\3+\7+\u011a\n+"+
		"\f+\16+\u011d\13+\3+\3+\3,\3,\3-\6-\u0124\n-\r-\16-\u0125\3-\3-\4\u010d"+
		"\u011b\2.\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2"+
		"\35\2\37\2!\2#\3%\4\'\5)\6+\7-\b/\t\61\n\63\13\65\f\67\r9\16;\17=\20?"+
		"\21A\22C\23E\24G\25I\26K\27M\30O\31Q\32S\33U\34W\35Y\36\3\2\r\3\2c|\3"+
		"\2C\\\3\2\62;\4\2GGgg\3\2\60\60\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^"+
		"\5\2\62;CHch\3\2\629\4\2\60\60AA\5\2\13\f\16\17\"\"\2\u0130\2#\3\2\2\2"+
		"\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2"+
		"\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2"+
		"\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2"+
		"I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3"+
		"\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3[\3\2\2\2\5]\3\2\2\2\7_\3\2\2\2\tc\3\2\2"+
		"\2\13e\3\2\2\2\rn\3\2\2\2\17v\3\2\2\2\21\u0081\3\2\2\2\23\u0084\3\2\2"+
		"\2\25\u0087\3\2\2\2\27\u008d\3\2\2\2\31\u008f\3\2\2\2\33\u0091\3\2\2\2"+
		"\35\u0097\3\2\2\2\37\u009f\3\2\2\2!\u00a7\3\2\2\2#\u00b1\3\2\2\2%\u00b3"+
		"\3\2\2\2\'\u00b5\3\2\2\2)\u00be\3\2\2\2+\u00c5\3\2\2\2-\u00c9\3\2\2\2"+
		"/\u00cf\3\2\2\2\61\u00d1\3\2\2\2\63\u00d3\3\2\2\2\65\u00d5\3\2\2\2\67"+
		"\u00d7\3\2\2\29\u00d9\3\2\2\2;\u00db\3\2\2\2=\u00dd\3\2\2\2?\u00df\3\2"+
		"\2\2A\u00e1\3\2\2\2C\u00e3\3\2\2\2E\u00e5\3\2\2\2G\u00e7\3\2\2\2I\u00e9"+
		"\3\2\2\2K\u00eb\3\2\2\2M\u00ed\3\2\2\2O\u00f5\3\2\2\2Q\u00fe\3\2\2\2S"+
		"\u0107\3\2\2\2U\u0115\3\2\2\2W\u0120\3\2\2\2Y\u0123\3\2\2\2[\\\t\2\2\2"+
		"\\\4\3\2\2\2]^\t\3\2\2^\6\3\2\2\2_`\t\4\2\2`\b\3\2\2\2ad\5\3\2\2bd\5\5"+
		"\3\2ca\3\2\2\2cb\3\2\2\2d\n\3\2\2\2eg\t\5\2\2fh\5\61\31\2gf\3\2\2\2gh"+
		"\3\2\2\2hj\3\2\2\2ik\5\7\4\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2m"+
		"\f\3\2\2\2nr\t\6\2\2oq\5\7\4\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2"+
		"s\16\3\2\2\2tr\3\2\2\2uw\5\7\4\2vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2"+
		"\2y\177\3\2\2\2z|\5\r\7\2{}\5\13\6\2|{\3\2\2\2|}\3\2\2\2}\u0080\3\2\2"+
		"\2~\u0080\5\13\6\2\177z\3\2\2\2\177~\3\2\2\2\u0080\20\3\2\2\2\u0081\u0082"+
		"\7^\2\2\u0082\u0083\n\7\2\2\u0083\22\3\2\2\2\u0084\u0085\7^\2\2\u0085"+
		"\u0086\t\7\2\2\u0086\24\3\2\2\2\u0087\u0088\7)\2\2\u0088\u0089\7$\2\2"+
		"\u0089\26\3\2\2\2\u008a\u008e\n\b\2\2\u008b\u008e\5\23\n\2\u008c\u008e"+
		"\5\25\13\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008c\3\2\2\2"+
		"\u008e\30\3\2\2\2\u008f\u0090\t\t\2\2\u0090\32\3\2\2\2\u0091\u0092\t\n"+
		"\2\2\u0092\34\3\2\2\2\u0093\u0094\7\62\2\2\u0094\u0098\7z\2\2\u0095\u0096"+
		"\7\62\2\2\u0096\u0098\7Z\2\2\u0097\u0093\3\2\2\2\u0097\u0095\3\2\2\2\u0098"+
		"\u009a\3\2\2\2\u0099\u009b\5\31\r\2\u009a\u0099\3\2\2\2\u009b\u009c\3"+
		"\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\36\3\2\2\2\u009e"+
		"\u00a0\5\7\4\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u009f\3\2"+
		"\2\2\u00a1\u00a2\3\2\2\2\u00a2 \3\2\2\2\u00a3\u00a4\7\62\2\2\u00a4\u00a8"+
		"\7q\2\2\u00a5\u00a6\7\62\2\2\u00a6\u00a8\7Q\2\2\u00a7\u00a3\3\2\2\2\u00a7"+
		"\u00a5\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00ab\5\33\16\2\u00aa\u00a9\3"+
		"\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad"+
		"\"\3\2\2\2\u00ae\u00b2\5\37\20\2\u00af\u00b2\5\35\17\2\u00b0\u00b2\5!"+
		"\21\2\u00b1\u00ae\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2"+
		"$\3\2\2\2\u00b3\u00b4\5\17\b\2\u00b4&\3\2\2\2\u00b5\u00b9\7$\2\2\u00b6"+
		"\u00b8\5\27\f\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3"+
		"\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc"+
		"\u00bd\7$\2\2\u00bd(\3\2\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7g\2\2\u00c0"+
		"\u00c1\7v\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7t\2\2\u00c3\u00c4\7p\2\2"+
		"\u00c4*\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7p\2\2\u00c7\u00c8\7v\2"+
		"\2\u00c8,\3\2\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7"+
		"q\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7v\2\2\u00ce.\3\2\2\2\u00cf\u00d0"+
		"\7-\2\2\u00d0\60\3\2\2\2\u00d1\u00d2\7/\2\2\u00d2\62\3\2\2\2\u00d3\u00d4"+
		"\7,\2\2\u00d4\64\3\2\2\2\u00d5\u00d6\7\61\2\2\u00d6\66\3\2\2\2\u00d7\u00d8"+
		"\7*\2\2\u00d88\3\2\2\2\u00d9\u00da\7+\2\2\u00da:\3\2\2\2\u00db\u00dc\7"+
		"]\2\2\u00dc<\3\2\2\2\u00dd\u00de\7_\2\2\u00de>\3\2\2\2\u00df\u00e0\7}"+
		"\2\2\u00e0@\3\2\2\2\u00e1\u00e2\7\177\2\2\u00e2B\3\2\2\2\u00e3\u00e4\7"+
		"<\2\2\u00e4D\3\2\2\2\u00e5\u00e6\7\60\2\2\u00e6F\3\2\2\2\u00e7\u00e8\7"+
		"=\2\2\u00e8H\3\2\2\2\u00e9\u00ea\7.\2\2\u00eaJ\3\2\2\2\u00eb\u00ec\7?"+
		"\2\2\u00ecL\3\2\2\2\u00ed\u00f2\5\3\2\2\u00ee\u00f1\5\3\2\2\u00ef\u00f1"+
		"\5\7\4\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2"+
		"\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3N\3\2\2\2\u00f4\u00f2\3\2\2\2"+
		"\u00f5\u00f9\7$\2\2\u00f6\u00f8\5\27\f\2\u00f7\u00f6\3\2\2\2\u00f8\u00fb"+
		"\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fc\3\2\2\2\u00fb"+
		"\u00f9\3\2\2\2\u00fc\u00fd\5\21\t\2\u00fdP\3\2\2\2\u00fe\u0102\7$\2\2"+
		"\u00ff\u0101\5\27\f\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100"+
		"\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2\u0104\u0102\3\2\2\2\u0105"+
		"\u0106\7\2\2\3\u0106R\3\2\2\2\u0107\u0108\7,\2\2\u0108\u0109\7,\2\2\u0109"+
		"\u010d\3\2\2\2\u010a\u010c\13\2\2\2\u010b\u010a\3\2\2\2\u010c\u010f\3"+
		"\2\2\2\u010d\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u0110\3\2\2\2\u010f"+
		"\u010d\3\2\2\2\u0110\u0111\7,\2\2\u0111\u0112\7,\2\2\u0112\u0113\3\2\2"+
		"\2\u0113\u0114\b*\2\2\u0114T\3\2\2\2\u0115\u0116\7,\2\2\u0116\u0117\7"+
		",\2\2\u0117\u011b\3\2\2\2\u0118\u011a\13\2\2\2\u0119\u0118\3\2\2\2\u011a"+
		"\u011d\3\2\2\2\u011b\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011e\3\2"+
		"\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7\2\2\3\u011fV\3\2\2\2\u0120\u0121"+
		"\t\13\2\2\u0121X\3\2\2\2\u0122\u0124\t\f\2\2\u0123\u0122\3\2\2\2\u0124"+
		"\u0125\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2"+
		"\2\2\u0127\u0128\b-\2\2\u0128Z\3\2\2\2\31\2cglrx|\177\u008d\u0097\u009c"+
		"\u00a1\u00a7\u00ac\u00b1\u00b9\u00f0\u00f2\u00f9\u0102\u010d\u011b\u0125"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}