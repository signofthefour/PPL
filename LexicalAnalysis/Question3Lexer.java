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
		T__0=1, Real_number=2, Integer_number=3, SEMI=4, COMMA=5, HEXADECIMAL=6, 
		DECIMAL=7, OCTAL=8, STRING=9, WS=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "Real_number", "Integer_number", "LOWERCASE_LETTER", "UPPERCASE_LETTER", 
			"DIGIT", "SIGN", "SPACE", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
			"SING_QUOTE", "DOUBLE_QUOTE", "DOUBLE_QUOTE_IN_QUOTE", "HEXADECIMALDIGIT", 
			"OCTALDIGIT", "COLON", "SEMI", "DOT", "COMMA", "HEXADECIMAL", "DECIMAL", 
			"OCTAL", "LETTER", "ID", "SING_QUOTE_IN_STRING", "STRING_CHAR", "STRING", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'''", null, null, "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "Real_number", "Integer_number", "SEMI", "COMMA", "HEXADECIMAL", 
			"DECIMAL", "OCTAL", "STRING", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f\u00ba\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\3\2\3\2\3\3\3\3\3\3"+
		"\3\4\3\4\3\4\3\4\5\4G\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\5\bP\n\b\3\t\3\t"+
		"\3\n\3\n\3\n\6\nW\n\n\r\n\16\nX\3\13\3\13\7\13]\n\13\f\13\16\13`\13\13"+
		"\3\f\6\fc\n\f\r\f\16\fd\3\f\3\f\5\fi\n\f\3\f\5\fl\n\f\3\r\3\r\3\16\3\16"+
		"\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\26\3\26\3\26\3\26\5\26\u0084\n\26\3\26\6\26\u0087\n\26\r\26\16\26\u0088"+
		"\3\27\6\27\u008c\n\27\r\27\16\27\u008d\3\30\3\30\3\30\3\30\5\30\u0094"+
		"\n\30\3\30\6\30\u0097\n\30\r\30\16\30\u0098\3\31\3\31\5\31\u009d\n\31"+
		"\3\32\3\32\3\32\7\32\u00a2\n\32\f\32\16\32\u00a5\13\32\3\33\3\33\3\33"+
		"\3\34\3\34\5\34\u00ac\n\34\3\35\7\35\u00af\n\35\f\35\16\35\u00b2\13\35"+
		"\3\36\6\36\u00b5\n\36\r\36\16\36\u00b6\3\36\3\36\2\2\37\3\3\5\4\7\5\t"+
		"\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\6\'\2"+
		")\7+\b-\t/\n\61\2\63\2\65\2\67\29\13;\f\3\2\20\3\2c|\3\2C\\\3\2\62;\4"+
		"\2--//\3\2\"\"\3\2gg\3\2\60\60\3\2))\3\2$$\4\2$$))\5\2\62;CHch\3\2\62"+
		"9\5\2\n\f\16\17))\5\2\13\f\17\17\"\"\2\u00b9\2\3\3\2\2\2\2\5\3\2\2\2\2"+
		"\7\3\2\2\2\2%\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\29\3"+
		"\2\2\2\2;\3\2\2\2\3=\3\2\2\2\5?\3\2\2\2\7B\3\2\2\2\tH\3\2\2\2\13J\3\2"+
		"\2\2\rL\3\2\2\2\17O\3\2\2\2\21Q\3\2\2\2\23S\3\2\2\2\25Z\3\2\2\2\27b\3"+
		"\2\2\2\31m\3\2\2\2\33o\3\2\2\2\35q\3\2\2\2\37s\3\2\2\2!u\3\2\2\2#w\3\2"+
		"\2\2%y\3\2\2\2\'{\3\2\2\2)}\3\2\2\2+\u0083\3\2\2\2-\u008b\3\2\2\2/\u0093"+
		"\3\2\2\2\61\u009c\3\2\2\2\63\u009e\3\2\2\2\65\u00a6\3\2\2\2\67\u00ab\3"+
		"\2\2\29\u00b0\3\2\2\2;\u00b4\3\2\2\2=>\7)\2\2>\4\3\2\2\2?@\5\17\b\2@A"+
		"\5\27\f\2A\6\3\2\2\2BF\5\17\b\2CG\5-\27\2DG\5+\26\2EG\5/\30\2FC\3\2\2"+
		"\2FD\3\2\2\2FE\3\2\2\2G\b\3\2\2\2HI\t\2\2\2I\n\3\2\2\2JK\t\3\2\2K\f\3"+
		"\2\2\2LM\t\4\2\2M\16\3\2\2\2NP\t\5\2\2ON\3\2\2\2OP\3\2\2\2P\20\3\2\2\2"+
		"QR\t\6\2\2R\22\3\2\2\2ST\t\7\2\2TV\5\17\b\2UW\5\r\7\2VU\3\2\2\2WX\3\2"+
		"\2\2XV\3\2\2\2XY\3\2\2\2Y\24\3\2\2\2Z^\t\b\2\2[]\5\r\7\2\\[\3\2\2\2]`"+
		"\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_\26\3\2\2\2`^\3\2\2\2ac\5\r\7\2ba\3\2\2"+
		"\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2ek\3\2\2\2fh\5\25\13\2gi\5\23\n\2hg\3"+
		"\2\2\2hi\3\2\2\2il\3\2\2\2jl\5\23\n\2kf\3\2\2\2kj\3\2\2\2l\30\3\2\2\2"+
		"mn\t\t\2\2n\32\3\2\2\2op\t\n\2\2p\34\3\2\2\2qr\t\13\2\2r\36\3\2\2\2st"+
		"\t\f\2\2t \3\2\2\2uv\t\r\2\2v\"\3\2\2\2wx\7<\2\2x$\3\2\2\2yz\7=\2\2z&"+
		"\3\2\2\2{|\7\60\2\2|(\3\2\2\2}~\7.\2\2~*\3\2\2\2\177\u0080\7\62\2\2\u0080"+
		"\u0084\7z\2\2\u0081\u0082\7\62\2\2\u0082\u0084\7Z\2\2\u0083\177\3\2\2"+
		"\2\u0083\u0081\3\2\2\2\u0084\u0086\3\2\2\2\u0085\u0087\5\37\20\2\u0086"+
		"\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2"+
		"\2\2\u0089,\3\2\2\2\u008a\u008c\5\r\7\2\u008b\u008a\3\2\2\2\u008c\u008d"+
		"\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e.\3\2\2\2\u008f"+
		"\u0090\7\62\2\2\u0090\u0094\7q\2\2\u0091\u0092\7\62\2\2\u0092\u0094\7"+
		"Q\2\2\u0093\u008f\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096\3\2\2\2\u0095"+
		"\u0097\5!\21\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2"+
		"\2\2\u0098\u0099\3\2\2\2\u0099\60\3\2\2\2\u009a\u009d\5\t\5\2\u009b\u009d"+
		"\5\13\6\2\u009c\u009a\3\2\2\2\u009c\u009b\3\2\2\2\u009d\62\3\2\2\2\u009e"+
		"\u00a3\5\t\5\2\u009f\u00a2\5\t\5\2\u00a0\u00a2\5\r\7\2\u00a1\u009f\3\2"+
		"\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3"+
		"\u00a4\3\2\2\2\u00a4\64\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\5\31\r"+
		"\2\u00a7\u00a8\5\31\r\2\u00a8\66\3\2\2\2\u00a9\u00ac\5\65\33\2\u00aa\u00ac"+
		"\n\16\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac8\3\2\2\2\u00ad"+
		"\u00af\5\67\34\2\u00ae\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3"+
		"\2\2\2\u00b0\u00b1\3\2\2\2\u00b1:\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5"+
		"\t\17\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2"+
		"\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b\36\2\2\u00b9<\3"+
		"\2\2\2\25\2FOX^dhk\u0083\u0088\u008d\u0093\u0098\u009c\u00a1\u00a3\u00ab"+
		"\u00b0\u00b6\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}