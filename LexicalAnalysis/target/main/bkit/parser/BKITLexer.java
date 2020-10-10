// Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
		STRING=1, REAL=2, INTEGER=3, Ids_list=4, COLON=5, SEMI=6, DOT=7, COMMA=8, 
		VAR=9, ILLEGAL_ESCAPE=10, WS=11, UNCLOSE_STRING=12, ERROR_CHAR=13, BLOCK_COMMENT=14, 
		UNTERMINATED_COMMENT=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"STRING", "REAL", "INTEGER", "Ids_list", "LOWERCASE_LETTER", "UPPERCASE_LETTER", 
			"DIGIT", "SIGN", "SPACE", "ESCAPE_SEQUENCE", "ESCAPE_ILLEGAL", "SCIENTIFIC", 
			"DECIMAL_POINT", "FLOATING_POINT_NUM", "SING_QUOTE", "DOUBLE_QUOTE", 
			"DOUBLE_QUOTE_IN_QUOTE", "HEXADECIMALDIGIT", "OCTALDIGIT", "COLON", "SEMI", 
			"DOT", "COMMA", "VAR", "HEXADECIMAL", "DECIMAL", "OCTAL", "LETTER", "STRING_CHAR", 
			"ID", "ILLEGAL_ESCAPE", "WS", "UNCLOSE_STRING", "ERROR_CHAR", "BLOCK_COMMENT", 
			"UNTERMINATED_COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "':'", "';'", "'.'", "','", "'Var'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "STRING", "REAL", "INTEGER", "Ids_list", "COLON", "SEMI", "DOT", 
			"COMMA", "VAR", "ILLEGAL_ESCAPE", "WS", "UNCLOSE_STRING", "ERROR_CHAR", 
			"BLOCK_COMMENT", "UNTERMINATED_COMMENT"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21\u010c\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3\2\7\2N\n\2\f\2\16\2Q\13\2\3\2"+
		"\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\\\n\4\3\5\3\5\3\5\3\5\7\5b\n\5\f"+
		"\5\16\5e\13\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\5\tn\n\t\3\n\3\n\3\13\3\13\3"+
		"\13\3\13\3\13\5\13w\n\13\3\f\3\f\5\f{\n\f\3\r\3\r\3\r\6\r\u0080\n\r\r"+
		"\r\16\r\u0081\3\16\3\16\7\16\u0086\n\16\f\16\16\16\u0089\13\16\3\17\6"+
		"\17\u008c\n\17\r\17\16\17\u008d\3\17\3\17\5\17\u0092\n\17\3\17\5\17\u0095"+
		"\n\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26"+
		"\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32"+
		"\u00b1\n\32\3\32\6\32\u00b4\n\32\r\32\16\32\u00b5\3\33\6\33\u00b9\n\33"+
		"\r\33\16\33\u00ba\3\34\3\34\3\34\3\34\5\34\u00c1\n\34\3\34\6\34\u00c4"+
		"\n\34\r\34\16\34\u00c5\3\35\3\35\5\35\u00ca\n\35\3\36\3\36\5\36\u00ce"+
		"\n\36\3\37\3\37\3\37\7\37\u00d3\n\37\f\37\16\37\u00d6\13\37\3 \3 \7 \u00da"+
		"\n \f \16 \u00dd\13 \3 \3 \3!\6!\u00e2\n!\r!\16!\u00e3\3!\3!\3\"\3\"\7"+
		"\"\u00ea\n\"\f\"\16\"\u00ed\13\"\3\"\5\"\u00f0\n\"\3#\3#\3$\3$\3$\3$\7"+
		"$\u00f8\n$\f$\16$\u00fb\13$\3$\3$\3$\3$\3$\3%\3%\3%\3%\7%\u0106\n%\f%"+
		"\16%\u0109\13%\3%\3%\4\u00f9\u0107\2&\3\3\5\4\7\5\t\6\13\2\r\2\17\2\21"+
		"\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\7+\b-\t/\n\61\13\63"+
		"\2\65\2\67\29\2;\2=\2?\fA\rC\16E\17G\20I\21\3\2\24\3\2c|\3\2C\\\3\2\62"+
		";\4\2--//\3\2\"\"\t\2))^^ddhhppttvv\6\2\n\f\16\17))^^\3\2^^\3\2gg\3\2"+
		"\60\60\3\2))\3\2$$\4\2$$))\5\2\62;CHch\3\2\629\6\2\n\f\16\17$$^^\5\2\13"+
		"\f\17\17\"\"\4\3\n\f\16\17\2\u0110\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2"+
		"\2\t\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2"+
		"\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\3K"+
		"\3\2\2\2\5T\3\2\2\2\7W\3\2\2\2\t]\3\2\2\2\13f\3\2\2\2\rh\3\2\2\2\17j\3"+
		"\2\2\2\21m\3\2\2\2\23o\3\2\2\2\25v\3\2\2\2\27z\3\2\2\2\31|\3\2\2\2\33"+
		"\u0083\3\2\2\2\35\u008b\3\2\2\2\37\u0096\3\2\2\2!\u0098\3\2\2\2#\u009a"+
		"\3\2\2\2%\u009c\3\2\2\2\'\u009e\3\2\2\2)\u00a0\3\2\2\2+\u00a2\3\2\2\2"+
		"-\u00a4\3\2\2\2/\u00a6\3\2\2\2\61\u00a8\3\2\2\2\63\u00b0\3\2\2\2\65\u00b8"+
		"\3\2\2\2\67\u00c0\3\2\2\29\u00c9\3\2\2\2;\u00cd\3\2\2\2=\u00cf\3\2\2\2"+
		"?\u00d7\3\2\2\2A\u00e1\3\2\2\2C\u00e7\3\2\2\2E\u00f1\3\2\2\2G\u00f3\3"+
		"\2\2\2I\u0101\3\2\2\2KO\7$\2\2LN\5;\36\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2"+
		"OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2RS\7$\2\2S\4\3\2\2\2TU\5\21\t\2UV\5\35\17"+
		"\2V\6\3\2\2\2W[\5\21\t\2X\\\5\65\33\2Y\\\5\63\32\2Z\\\5\67\34\2[X\3\2"+
		"\2\2[Y\3\2\2\2[Z\3\2\2\2\\\b\3\2\2\2]c\5=\37\2^_\5/\30\2_`\5=\37\2`b\3"+
		"\2\2\2a^\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2d\n\3\2\2\2ec\3\2\2\2fg"+
		"\t\2\2\2g\f\3\2\2\2hi\t\3\2\2i\16\3\2\2\2jk\t\4\2\2k\20\3\2\2\2ln\t\5"+
		"\2\2ml\3\2\2\2mn\3\2\2\2n\22\3\2\2\2op\t\6\2\2p\24\3\2\2\2qr\7^\2\2rw"+
		"\t\7\2\2st\5\37\20\2tu\5!\21\2uw\3\2\2\2vq\3\2\2\2vs\3\2\2\2w\26\3\2\2"+
		"\2x{\t\b\2\2y{\n\t\2\2zx\3\2\2\2zy\3\2\2\2{\30\3\2\2\2|}\t\n\2\2}\177"+
		"\5\21\t\2~\u0080\5\17\b\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\177\3"+
		"\2\2\2\u0081\u0082\3\2\2\2\u0082\32\3\2\2\2\u0083\u0087\t\13\2\2\u0084"+
		"\u0086\5\17\b\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3"+
		"\2\2\2\u0087\u0088\3\2\2\2\u0088\34\3\2\2\2\u0089\u0087\3\2\2\2\u008a"+
		"\u008c\5\17\b\2\u008b\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008b\3"+
		"\2\2\2\u008d\u008e\3\2\2\2\u008e\u0094\3\2\2\2\u008f\u0091\5\33\16\2\u0090"+
		"\u0092\5\31\r\2\u0091\u0090\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0095\3"+
		"\2\2\2\u0093\u0095\5\31\r\2\u0094\u008f\3\2\2\2\u0094\u0093\3\2\2\2\u0095"+
		"\36\3\2\2\2\u0096\u0097\t\f\2\2\u0097 \3\2\2\2\u0098\u0099\t\r\2\2\u0099"+
		"\"\3\2\2\2\u009a\u009b\t\16\2\2\u009b$\3\2\2\2\u009c\u009d\t\17\2\2\u009d"+
		"&\3\2\2\2\u009e\u009f\t\20\2\2\u009f(\3\2\2\2\u00a0\u00a1\7<\2\2\u00a1"+
		"*\3\2\2\2\u00a2\u00a3\7=\2\2\u00a3,\3\2\2\2\u00a4\u00a5\7\60\2\2\u00a5"+
		".\3\2\2\2\u00a6\u00a7\7.\2\2\u00a7\60\3\2\2\2\u00a8\u00a9\7X\2\2\u00a9"+
		"\u00aa\7c\2\2\u00aa\u00ab\7t\2\2\u00ab\62\3\2\2\2\u00ac\u00ad\7\62\2\2"+
		"\u00ad\u00b1\7z\2\2\u00ae\u00af\7\62\2\2\u00af\u00b1\7Z\2\2\u00b0\u00ac"+
		"\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b4\5%\23\2\u00b3"+
		"\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2"+
		"\2\2\u00b6\64\3\2\2\2\u00b7\u00b9\5\17\b\2\u00b8\u00b7\3\2\2\2\u00b9\u00ba"+
		"\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\66\3\2\2\2\u00bc"+
		"\u00bd\7\62\2\2\u00bd\u00c1\7q\2\2\u00be\u00bf\7\62\2\2\u00bf\u00c1\7"+
		"Q\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2"+
		"\u00c4\5\'\24\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c3\3"+
		"\2\2\2\u00c5\u00c6\3\2\2\2\u00c68\3\2\2\2\u00c7\u00ca\5\13\6\2\u00c8\u00ca"+
		"\5\r\7\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca:\3\2\2\2\u00cb"+
		"\u00ce\n\21\2\2\u00cc\u00ce\5\25\13\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc"+
		"\3\2\2\2\u00ce<\3\2\2\2\u00cf\u00d4\5\13\6\2\u00d0\u00d3\5\13\6\2\u00d1"+
		"\u00d3\5\17\b\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\u00d6\3"+
		"\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5>\3\2\2\2\u00d6\u00d4"+
		"\3\2\2\2\u00d7\u00db\7$\2\2\u00d8\u00da\5;\36\2\u00d9\u00d8\3\2\2\2\u00da"+
		"\u00dd\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de\3\2"+
		"\2\2\u00dd\u00db\3\2\2\2\u00de\u00df\5\27\f\2\u00df@\3\2\2\2\u00e0\u00e2"+
		"\t\22\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e1\3\2\2\2"+
		"\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\b!\2\2\u00e6B\3\2"+
		"\2\2\u00e7\u00eb\7$\2\2\u00e8\u00ea\5;\36\2\u00e9\u00e8\3\2\2\2\u00ea"+
		"\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ef\3\2"+
		"\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\t\23\2\2\u00ef\u00ee\3\2\2\2\u00f0"+
		"D\3\2\2\2\u00f1\u00f2\13\2\2\2\u00f2F\3\2\2\2\u00f3\u00f4\7,\2\2\u00f4"+
		"\u00f5\7,\2\2\u00f5\u00f9\3\2\2\2\u00f6\u00f8\13\2\2\2\u00f7\u00f6\3\2"+
		"\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00fa\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa"+
		"\u00fc\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fc\u00fd\7,\2\2\u00fd\u00fe\7,\2"+
		"\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\b$\3\2\u0100H\3\2\2\2\u0101\u0102\7"+
		",\2\2\u0102\u0103\7,\2\2\u0103\u0107\3\2\2\2\u0104\u0106\13\2\2\2\u0105"+
		"\u0104\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0108\3\2\2\2\u0107\u0105\3\2"+
		"\2\2\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\7\2\2\3\u010b"+
		"J\3\2\2\2\35\2O[cmvz\u0081\u0087\u008d\u0091\u0094\u00b0\u00b5\u00ba\u00c0"+
		"\u00c5\u00c9\u00cd\u00d2\u00d4\u00db\u00e3\u00eb\u00ef\u00f9\u0107\4\b"+
		"\2\2\2\3\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}