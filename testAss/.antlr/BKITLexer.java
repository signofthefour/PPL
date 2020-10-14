// Generated from /home/khanh/Documents/schoolLife/201/PPL/testAss/BKIT.g4 by ANTLR 4.8
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
		VAR=1, FUNCTION=2, BODY=3, ELSE=4, ENDFOR=5, IF=6, ENDDO=7, BREAK=8, ELSEIF=9, 
		ENDWHILE=10, PARAMETER=11, WHILE=12, CONTINUE=13, ENDBODY=14, FOR=15, 
		RETURN=16, TRUE=17, DO=18, ENDIF=19, THEN=20, FALSE=21, WS=22, IDENTIFIER=23, 
		LB=24, RB=25, LK=26, RK=27, LP=28, RP=29, SEMI=30, COLON=31, CM=32, DOT=33, 
		INTEGER=34, FLOAT=35, BOLEAN=36, ADDOP=37, SUBOP=38, MULOP=39, DIVOP=40, 
		AS=41, ERROR_CHAR=42, UNCLOSE_STRING=43, ILLEGAL_ESCAPE=44, UNTERMINATED_COMMENT=45;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", 
			"ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
			"RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "WS", "IDENTIFIER", 
			"LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "INTEGER", 
			"FLOAT", "BOLEAN", "ADDOP", "SUBOP", "MULOP", "DIVOP", "AS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "LETTER", 
			"UPCASE_LETTER", "NUMBER", "EXPO", "SIGN", "SCIEN", "HEX", "OCTA"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Var'", "'Function:'", "'Body'", "'Else'", "'EndFor'", "'If'", 
			"'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
			"'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", 
			"'Then'", "'False'", null, null, "'{'", "'}'", "'['", "']'", "'('", "')'", 
			"';'", "':'", "','", "'.'", null, null, null, "'+'", "'-'", "'*'", "'/'", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", 
			"ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
			"RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "WS", "IDENTIFIER", 
			"LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "INTEGER", 
			"FLOAT", "BOLEAN", "ADDOP", "SUBOP", "MULOP", "DIVOP", "AS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/\u016e\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16"+
		"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\6\27\u00f2\n\27"+
		"\r\27\16\27\u00f3\3\27\3\27\3\30\3\30\3\30\3\30\3\30\7\30\u00fd\n\30\f"+
		"\30\16\30\u0100\13\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35"+
		"\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\6#\u0117\n#\r#\16#\u0118\3"+
		"#\3#\6#\u011d\n#\r#\16#\u011e\3#\3#\6#\u0123\n#\r#\16#\u0124\5#\u0127"+
		"\n#\3$\6$\u012a\n$\r$\16$\u012b\3$\3$\7$\u0130\n$\f$\16$\u0133\13$\3$"+
		"\5$\u0136\n$\3$\5$\u0139\n$\3%\3%\5%\u013d\n%\3&\3&\3\'\3\'\3(\3(\3)\3"+
		")\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3"+
		"\62\3\63\5\63\u015b\n\63\3\64\3\64\6\64\u015f\n\64\r\64\16\64\u0160\3"+
		"\65\3\65\3\65\3\65\5\65\u0167\n\65\3\66\3\66\3\66\3\66\5\66\u016d\n\66"+
		"\2\2\67\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17"+
		"\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35"+
		"9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\2e\2g\2i\2k\2\3\2"+
		"\n\5\2\13\f\17\17\"\"\4\2\62;CH\3\2\629\3\2c|\3\2C\\\3\2\62;\4\2GGgg\4"+
		"\2--//\2\u0179\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2"+
		"\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2"+
		"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3"+
		"\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2"+
		"\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\3m\3\2\2\2\5"+
		"q\3\2\2\2\7{\3\2\2\2\t\u0080\3\2\2\2\13\u0085\3\2\2\2\r\u008c\3\2\2\2"+
		"\17\u008f\3\2\2\2\21\u0095\3\2\2\2\23\u009b\3\2\2\2\25\u00a2\3\2\2\2\27"+
		"\u00ab\3\2\2\2\31\u00b5\3\2\2\2\33\u00bb\3\2\2\2\35\u00c4\3\2\2\2\37\u00cc"+
		"\3\2\2\2!\u00d0\3\2\2\2#\u00d7\3\2\2\2%\u00dc\3\2\2\2\'\u00df\3\2\2\2"+
		")\u00e5\3\2\2\2+\u00ea\3\2\2\2-\u00f1\3\2\2\2/\u00f7\3\2\2\2\61\u0101"+
		"\3\2\2\2\63\u0103\3\2\2\2\65\u0105\3\2\2\2\67\u0107\3\2\2\29\u0109\3\2"+
		"\2\2;\u010b\3\2\2\2=\u010d\3\2\2\2?\u010f\3\2\2\2A\u0111\3\2\2\2C\u0113"+
		"\3\2\2\2E\u0126\3\2\2\2G\u0129\3\2\2\2I\u013c\3\2\2\2K\u013e\3\2\2\2M"+
		"\u0140\3\2\2\2O\u0142\3\2\2\2Q\u0144\3\2\2\2S\u0146\3\2\2\2U\u0148\3\2"+
		"\2\2W\u014a\3\2\2\2Y\u014c\3\2\2\2[\u014e\3\2\2\2]\u0150\3\2\2\2_\u0152"+
		"\3\2\2\2a\u0154\3\2\2\2c\u0156\3\2\2\2e\u015a\3\2\2\2g\u015c\3\2\2\2i"+
		"\u0166\3\2\2\2k\u016c\3\2\2\2mn\7X\2\2no\7c\2\2op\7t\2\2p\4\3\2\2\2qr"+
		"\7H\2\2rs\7w\2\2st\7p\2\2tu\7e\2\2uv\7v\2\2vw\7k\2\2wx\7q\2\2xy\7p\2\2"+
		"yz\7<\2\2z\6\3\2\2\2{|\7D\2\2|}\7q\2\2}~\7f\2\2~\177\7{\2\2\177\b\3\2"+
		"\2\2\u0080\u0081\7G\2\2\u0081\u0082\7n\2\2\u0082\u0083\7u\2\2\u0083\u0084"+
		"\7g\2\2\u0084\n\3\2\2\2\u0085\u0086\7G\2\2\u0086\u0087\7p\2\2\u0087\u0088"+
		"\7f\2\2\u0088\u0089\7H\2\2\u0089\u008a\7q\2\2\u008a\u008b\7t\2\2\u008b"+
		"\f\3\2\2\2\u008c\u008d\7K\2\2\u008d\u008e\7h\2\2\u008e\16\3\2\2\2\u008f"+
		"\u0090\7G\2\2\u0090\u0091\7p\2\2\u0091\u0092\7f\2\2\u0092\u0093\7F\2\2"+
		"\u0093\u0094\7q\2\2\u0094\20\3\2\2\2\u0095\u0096\7D\2\2\u0096\u0097\7"+
		"t\2\2\u0097\u0098\7g\2\2\u0098\u0099\7c\2\2\u0099\u009a\7m\2\2\u009a\22"+
		"\3\2\2\2\u009b\u009c\7G\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e"+
		"\u009f\7g\2\2\u009f\u00a0\7K\2\2\u00a0\u00a1\7h\2\2\u00a1\24\3\2\2\2\u00a2"+
		"\u00a3\7G\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5\7f\2\2\u00a5\u00a6\7Y\2\2"+
		"\u00a6\u00a7\7j\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7n\2\2\u00a9\u00aa"+
		"\7g\2\2\u00aa\26\3\2\2\2\u00ab\u00ac\7R\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae"+
		"\7t\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7o\2\2\u00b0\u00b1\7g\2\2\u00b1"+
		"\u00b2\7v\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7t\2\2\u00b4\30\3\2\2\2\u00b5"+
		"\u00b6\7Y\2\2\u00b6\u00b7\7j\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7n\2\2"+
		"\u00b9\u00ba\7g\2\2\u00ba\32\3\2\2\2\u00bb\u00bc\7E\2\2\u00bc\u00bd\7"+
		"q\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7k\2\2\u00c0\u00c1"+
		"\7p\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7g\2\2\u00c3\34\3\2\2\2\u00c4\u00c5"+
		"\7G\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7D\2\2\u00c8"+
		"\u00c9\7q\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb\7{\2\2\u00cb\36\3\2\2\2\u00cc"+
		"\u00cd\7H\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7t\2\2\u00cf \3\2\2\2\u00d0"+
		"\u00d1\7T\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7w\2\2"+
		"\u00d4\u00d5\7t\2\2\u00d5\u00d6\7p\2\2\u00d6\"\3\2\2\2\u00d7\u00d8\7V"+
		"\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7g\2\2\u00db$\3"+
		"\2\2\2\u00dc\u00dd\7F\2\2\u00dd\u00de\7q\2\2\u00de&\3\2\2\2\u00df\u00e0"+
		"\7G\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7f\2\2\u00e2\u00e3\7K\2\2\u00e3"+
		"\u00e4\7h\2\2\u00e4(\3\2\2\2\u00e5\u00e6\7V\2\2\u00e6\u00e7\7j\2\2\u00e7"+
		"\u00e8\7g\2\2\u00e8\u00e9\7p\2\2\u00e9*\3\2\2\2\u00ea\u00eb\7H\2\2\u00eb"+
		"\u00ec\7c\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef\7g\2\2"+
		"\u00ef,\3\2\2\2\u00f0\u00f2\t\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3"+
		"\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5"+
		"\u00f6\b\27\2\2\u00f6.\3\2\2\2\u00f7\u00fe\5]/\2\u00f8\u00fd\5]/\2\u00f9"+
		"\u00fd\5_\60\2\u00fa\u00fd\5a\61\2\u00fb\u00fd\7a\2\2\u00fc\u00f8\3\2"+
		"\2\2\u00fc\u00f9\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd"+
		"\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\60\3\2\2"+
		"\2\u0100\u00fe\3\2\2\2\u0101\u0102\7}\2\2\u0102\62\3\2\2\2\u0103\u0104"+
		"\7\177\2\2\u0104\64\3\2\2\2\u0105\u0106\7]\2\2\u0106\66\3\2\2\2\u0107"+
		"\u0108\7_\2\2\u01088\3\2\2\2\u0109\u010a\7*\2\2\u010a:\3\2\2\2\u010b\u010c"+
		"\7+\2\2\u010c<\3\2\2\2\u010d\u010e\7=\2\2\u010e>\3\2\2\2\u010f\u0110\7"+
		"<\2\2\u0110@\3\2\2\2\u0111\u0112\7.\2\2\u0112B\3\2\2\2\u0113\u0114\7\60"+
		"\2\2\u0114D\3\2\2\2\u0115\u0117\5a\61\2\u0116\u0115\3\2\2\2\u0117\u0118"+
		"\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u0127\3\2\2\2\u011a"+
		"\u011c\5i\65\2\u011b\u011d\t\3\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2"+
		"\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0127\3\2\2\2\u0120"+
		"\u0122\5k\66\2\u0121\u0123\t\4\2\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2"+
		"\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126"+
		"\u0116\3\2\2\2\u0126\u011a\3\2\2\2\u0126\u0120\3\2\2\2\u0127F\3\2\2\2"+
		"\u0128\u012a\5a\61\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0129"+
		"\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u0138\3\2\2\2\u012d\u0131\5C\"\2\u012e"+
		"\u0130\5a\61\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3\2"+
		"\2\2\u0131\u0132\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0134"+
		"\u0136\5g\64\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0139\3\2"+
		"\2\2\u0137\u0139\5g\64\2\u0138\u012d\3\2\2\2\u0138\u0137\3\2\2\2\u0138"+
		"\u0139\3\2\2\2\u0139H\3\2\2\2\u013a\u013d\5#\22\2\u013b\u013d\5+\26\2"+
		"\u013c\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013dJ\3\2\2\2\u013e\u013f\7"+
		"-\2\2\u013fL\3\2\2\2\u0140\u0141\7/\2\2\u0141N\3\2\2\2\u0142\u0143\7,"+
		"\2\2\u0143P\3\2\2\2\u0144\u0145\7\61\2\2\u0145R\3\2\2\2\u0146\u0147\7"+
		"?\2\2\u0147T\3\2\2\2\u0148\u0149\13\2\2\2\u0149V\3\2\2\2\u014a\u014b\13"+
		"\2\2\2\u014bX\3\2\2\2\u014c\u014d\13\2\2\2\u014dZ\3\2\2\2\u014e\u014f"+
		"\13\2\2\2\u014f\\\3\2\2\2\u0150\u0151\t\5\2\2\u0151^\3\2\2\2\u0152\u0153"+
		"\t\6\2\2\u0153`\3\2\2\2\u0154\u0155\t\7\2\2\u0155b\3\2\2\2\u0156\u0157"+
		"\t\b\2\2\u0157\u0158\5e\63\2\u0158d\3\2\2\2\u0159\u015b\t\t\2\2\u015a"+
		"\u0159\3\2\2\2\u015a\u015b\3\2\2\2\u015bf\3\2\2\2\u015c\u015e\5c\62\2"+
		"\u015d\u015f\5a\61\2\u015e\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u015e"+
		"\3\2\2\2\u0160\u0161\3\2\2\2\u0161h\3\2\2\2\u0162\u0163\7\62\2\2\u0163"+
		"\u0167\7z\2\2\u0164\u0165\7\62\2\2\u0165\u0167\7Z\2\2\u0166\u0162\3\2"+
		"\2\2\u0166\u0164\3\2\2\2\u0167j\3\2\2\2\u0168\u0169\7\62\2\2\u0169\u016d"+
		"\7q\2\2\u016a\u016b\7\62\2\2\u016b\u016d\7Q\2\2\u016c\u0168\3\2\2\2\u016c"+
		"\u016a\3\2\2\2\u016dl\3\2\2\2\23\2\u00f3\u00fc\u00fe\u0118\u011e\u0124"+
		"\u0126\u012b\u0131\u0135\u0138\u013c\u015a\u0160\u0166\u016c\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}