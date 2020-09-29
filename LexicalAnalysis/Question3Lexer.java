// Generated from Question3.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class Question3Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, Real_number=2, Integer_number=3, String=4, HEXADECIMAL=5, DECIMAL=6, 
		OCTAL=7, LETTER=8, PUNCTUATION=9, ID=10, WS=11;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "Real_number", "Integer_number", "String", "LOWERCASE_LETTER", 
			"UPPERCASE_LETTER", "DIGIT", "SIGN", "SPACE", "ESCAPE_SEQUENCE", "SCIENTIFIC", 
			"DECIMAL_POINT", "FLOATING_POINT_NUM", "SING_QUOTE", "DOUBLE_QUOTE", 
			"DOUBLE_QUOTE_IN_QUOTE", "HEXADECIMALDIGIT", "OCTALDIGIT", "COLON", "SEMI", 
			"DOT", "COMMA", "HEXADECIMAL", "DECIMAL", "OCTAL", "LETTER", "PUNCTUATION", 
			"ID", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "Real_number", "Integer_number", "String", "HEXADECIMAL", 
			"DECIMAL", "OCTAL", "LETTER", "PUNCTUATION", "ID", "WS"
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


	public Question3Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Question3.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r\u00d3\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\3\3\3\3\3"+
		"\3\4\3\4\3\4\3\4\5\4G\n\4\3\5\6\5J\n\5\r\5\16\5K\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\6\5X\n\5\r\5\16\5Y\3\6\3\6\3\7\3\7\3\b\3\b\3\t\5\t"+
		"c\n\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\5\13s\n\13\3\f\3\f\3\f\6\fx\n\f\r\f\16\fy\3\r\3\r\7\r~\n\r\f\r\16"+
		"\r\u0081\13\r\3\16\6\16\u0084\n\16\r\16\16\16\u0085\3\16\3\16\5\16\u008a"+
		"\n\16\3\16\5\16\u008d\n\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23"+
		"\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\5\30"+
		"\u00a5\n\30\3\30\6\30\u00a8\n\30\r\30\16\30\u00a9\3\31\6\31\u00ad\n\31"+
		"\r\31\16\31\u00ae\3\32\3\32\3\32\3\32\5\32\u00b5\n\32\3\32\6\32\u00b8"+
		"\n\32\r\32\16\32\u00b9\3\33\3\33\5\33\u00be\n\33\3\34\3\34\3\34\3\34\5"+
		"\34\u00c4\n\34\3\35\3\35\3\35\6\35\u00c9\n\35\r\35\16\35\u00ca\3\36\6"+
		"\36\u00ce\n\36\r\36\16\36\u00cf\3\36\3\36\2\2\37\3\3\5\4\7\5\t\6\13\2"+
		"\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-"+
		"\2/\7\61\b\63\t\65\n\67\139\f;\r\3\2\17\3\2c|\3\2C\\\3\2\62;\4\2--//\3"+
		"\2\"\"\3\2gg\3\2\60\60\3\2))\3\2$$\4\2$$))\5\2\62;CHch\3\2\629\5\2\13"+
		"\f\17\17\"\"\2\u00e1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2"+
		"/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2"+
		"\2\2;\3\2\2\2\3=\3\2\2\2\5?\3\2\2\2\7B\3\2\2\2\tW\3\2\2\2\13[\3\2\2\2"+
		"\r]\3\2\2\2\17_\3\2\2\2\21b\3\2\2\2\23d\3\2\2\2\25r\3\2\2\2\27t\3\2\2"+
		"\2\31{\3\2\2\2\33\u0083\3\2\2\2\35\u008e\3\2\2\2\37\u0090\3\2\2\2!\u0092"+
		"\3\2\2\2#\u0094\3\2\2\2%\u0096\3\2\2\2\'\u0098\3\2\2\2)\u009a\3\2\2\2"+
		"+\u009c\3\2\2\2-\u009e\3\2\2\2/\u00a4\3\2\2\2\61\u00ac\3\2\2\2\63\u00b4"+
		"\3\2\2\2\65\u00bd\3\2\2\2\67\u00c3\3\2\2\29\u00c5\3\2\2\2;\u00cd\3\2\2"+
		"\2=>\7$\2\2>\4\3\2\2\2?@\5\21\t\2@A\5\33\16\2A\6\3\2\2\2BF\5\21\t\2CG"+
		"\5\61\31\2DG\5/\30\2EG\5\63\32\2FC\3\2\2\2FD\3\2\2\2FE\3\2\2\2G\b\3\2"+
		"\2\2HJ\5\65\33\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LX\3\2\2\2MX\5"+
		"\25\13\2NO\5\35\17\2OP\5\37\20\2PX\3\2\2\2QX\5\17\b\2RX\5\67\34\2ST\5"+
		"\35\17\2TU\5\35\17\2UX\3\2\2\2VX\5\23\n\2WI\3\2\2\2WM\3\2\2\2WN\3\2\2"+
		"\2WQ\3\2\2\2WR\3\2\2\2WS\3\2\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2"+
		"\2Z\n\3\2\2\2[\\\t\2\2\2\\\f\3\2\2\2]^\t\3\2\2^\16\3\2\2\2_`\t\4\2\2`"+
		"\20\3\2\2\2ac\t\5\2\2ba\3\2\2\2bc\3\2\2\2c\22\3\2\2\2de\t\6\2\2e\24\3"+
		"\2\2\2fg\7^\2\2gs\7)\2\2hi\7^\2\2is\7d\2\2jk\7^\2\2ks\7h\2\2lm\7^\2\2"+
		"ms\7p\2\2no\7^\2\2os\7t\2\2pq\7^\2\2qs\7v\2\2rf\3\2\2\2rh\3\2\2\2rj\3"+
		"\2\2\2rl\3\2\2\2rn\3\2\2\2rp\3\2\2\2s\26\3\2\2\2tu\t\7\2\2uw\5\21\t\2"+
		"vx\5\17\b\2wv\3\2\2\2xy\3\2\2\2yw\3\2\2\2yz\3\2\2\2z\30\3\2\2\2{\177\t"+
		"\b\2\2|~\5\17\b\2}|\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2"+
		"\2\2\u0080\32\3\2\2\2\u0081\177\3\2\2\2\u0082\u0084\5\17\b\2\u0083\u0082"+
		"\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086"+
		"\u008c\3\2\2\2\u0087\u0089\5\31\r\2\u0088\u008a\5\27\f\2\u0089\u0088\3"+
		"\2\2\2\u0089\u008a\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u008d\5\27\f\2\u008c"+
		"\u0087\3\2\2\2\u008c\u008b\3\2\2\2\u008d\34\3\2\2\2\u008e\u008f\t\t\2"+
		"\2\u008f\36\3\2\2\2\u0090\u0091\t\n\2\2\u0091 \3\2\2\2\u0092\u0093\t\13"+
		"\2\2\u0093\"\3\2\2\2\u0094\u0095\t\f\2\2\u0095$\3\2\2\2\u0096\u0097\t"+
		"\r\2\2\u0097&\3\2\2\2\u0098\u0099\7<\2\2\u0099(\3\2\2\2\u009a\u009b\7"+
		"=\2\2\u009b*\3\2\2\2\u009c\u009d\7\60\2\2\u009d,\3\2\2\2\u009e\u009f\7"+
		".\2\2\u009f.\3\2\2\2\u00a0\u00a1\7\62\2\2\u00a1\u00a5\7z\2\2\u00a2\u00a3"+
		"\7\62\2\2\u00a3\u00a5\7Z\2\2\u00a4\u00a0\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5"+
		"\u00a7\3\2\2\2\u00a6\u00a8\5#\22\2\u00a7\u00a6\3\2\2\2\u00a8\u00a9\3\2"+
		"\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\60\3\2\2\2\u00ab\u00ad"+
		"\5\17\b\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2"+
		"\u00ae\u00af\3\2\2\2\u00af\62\3\2\2\2\u00b0\u00b1\7\62\2\2\u00b1\u00b5"+
		"\7q\2\2\u00b2\u00b3\7\62\2\2\u00b3\u00b5\7Q\2\2\u00b4\u00b0\3\2\2\2\u00b4"+
		"\u00b2\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b8\5%\23\2\u00b7\u00b6\3\2"+
		"\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba"+
		"\64\3\2\2\2\u00bb\u00be\5\13\6\2\u00bc\u00be\5\r\7\2\u00bd\u00bb\3\2\2"+
		"\2\u00bd\u00bc\3\2\2\2\u00be\66\3\2\2\2\u00bf\u00c4\5\'\24\2\u00c0\u00c4"+
		"\5)\25\2\u00c1\u00c4\5+\26\2\u00c2\u00c4\5-\27\2\u00c3\u00bf\3\2\2\2\u00c3"+
		"\u00c0\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2\3\2\2\2\u00c48\3\2\2\2"+
		"\u00c5\u00c8\5\13\6\2\u00c6\u00c9\5\13\6\2\u00c7\u00c9\5\17\b\2\u00c8"+
		"\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2"+
		"\2\2\u00ca\u00cb\3\2\2\2\u00cb:\3\2\2\2\u00cc\u00ce\t\16\2\2\u00cd\u00cc"+
		"\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0"+
		"\u00d1\3\2\2\2\u00d1\u00d2\b\36\2\2\u00d2<\3\2\2\2\30\2FKWYbry\177\u0085"+
		"\u0089\u008c\u00a4\u00a9\u00ae\u00b4\u00b9\u00bd\u00c3\u00c8\u00ca\u00cf"+
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