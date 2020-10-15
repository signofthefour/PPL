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
		DOUQUO=34, INTEGER=35, FLOAT=36, BOLEAN=37, FADDOP=38, IADDOP=39, FSUBOP=40, 
		ISUBOP=41, FMULOP=42, IMULOP=43, FDIVOP=44, IDIVOP=45, IREMAIN=46, EQUAL=47, 
		FNEQUAL=48, FLESSOE=49, FGROE=50, FLESS=51, FGR=52, INEQUAL=53, ILESSOE=54, 
		IGROE=55, ILESS=56, IGR=57, BNEG=58, BAND=59, BOR=60, AS=61, STRING=62;
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
			"LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "DOUQUO", 
			"INTEGER", "FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", 
			"FMULOP", "IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", 
			"FLESSOE", "FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", 
			"IGR", "BNEG", "BAND", "BOR", "AS", "LETTER", "UPCASE_LETTER", "NUMBER", 
			"EXPO", "SIGN", "SCIEN", "HEX", "OCTA", "SDOUQUO", "SINGQUO", "STRING"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Var'", "'Function:'", "'Body'", "'Else'", "'EndFor'", "'If'", 
			"'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
			"'Continue'", "'EndBody.'", "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", 
			"'Then'", "'False'", null, null, "'{'", "'}'", "'['", "']'", "'('", "')'", 
			"';'", "':'", "','", "'.'", "'\"'", null, null, null, "'+.'", "'+'", 
			"'-.'", "'-'", "'*.'", "'*'", "'\\.'", "'\\'", "'%'", "'=='", "'=/='", 
			"'<=.'", "'>=.'", "'<.'", "'>.'", "'!='", "'<='", "'>='", "'<'", "'>'", 
			"'!'", "'&&'", "'||'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", 
			"ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
			"RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "WS", "IDENTIFIER", 
			"LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "DOUQUO", 
			"INTEGER", "FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", 
			"FMULOP", "IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", 
			"FLESSOE", "FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", 
			"IGR", "BNEG", "BAND", "BOR", "AS", "STRING"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@\u01d5\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20"+
		"\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22"+
		"\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25"+
		"\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\6\27\u0119\n\27\r\27\16\27\u011a"+
		"\3\27\3\27\3\30\3\30\3\30\3\30\3\30\7\30\u0124\n\30\f\30\16\30\u0127\13"+
		"\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3"+
		"\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\6$\u0140\n$\r$\16$\u0141\3$\3$\6$\u0146"+
		"\n$\r$\16$\u0147\3$\3$\6$\u014c\n$\r$\16$\u014d\5$\u0150\n$\3%\6%\u0153"+
		"\n%\r%\16%\u0154\3%\3%\7%\u0159\n%\f%\16%\u015c\13%\3%\5%\u015f\n%\3%"+
		"\5%\u0162\n%\3&\3&\5&\u0166\n&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+"+
		"\3+\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62"+
		"\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66"+
		"\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\3=\3=\3"+
		"=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\5C\u01b4\nC\3D\3D\6D\u01b8\nD\r"+
		"D\16D\u01b9\3E\3E\3E\3E\5E\u01c0\nE\3F\3F\3F\3F\5F\u01c6\nF\3G\3G\3G\3"+
		"H\3H\3I\3I\5I\u01cf\nI\7I\u01d1\nI\fI\16I\u01d4\13I\2\2J\3\3\5\4\7\5\t"+
		"\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{"+
		"?}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f"+
		"\2\u0091@\3\2\13\5\2\13\f\17\17\"\"\4\2\62;CH\3\2\629\3\2c|\3\2C\\\3\2"+
		"\62;\4\2GGgg\4\2--//\3\2$$\2\u01e1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2"+
		"\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3"+
		"\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2"+
		"\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2"+
		"\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2"+
		"\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2"+
		"\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2"+
		"O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3"+
		"\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2"+
		"\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2"+
		"u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2"+
		"\2\2\5\u0097\3\2\2\2\7\u00a1\3\2\2\2\t\u00a6\3\2\2\2\13\u00ab\3\2\2\2"+
		"\r\u00b2\3\2\2\2\17\u00b5\3\2\2\2\21\u00bb\3\2\2\2\23\u00c1\3\2\2\2\25"+
		"\u00c8\3\2\2\2\27\u00d1\3\2\2\2\31\u00db\3\2\2\2\33\u00e1\3\2\2\2\35\u00ea"+
		"\3\2\2\2\37\u00f3\3\2\2\2!\u00f7\3\2\2\2#\u00fe\3\2\2\2%\u0103\3\2\2\2"+
		"\'\u0106\3\2\2\2)\u010c\3\2\2\2+\u0111\3\2\2\2-\u0118\3\2\2\2/\u011e\3"+
		"\2\2\2\61\u0128\3\2\2\2\63\u012a\3\2\2\2\65\u012c\3\2\2\2\67\u012e\3\2"+
		"\2\29\u0130\3\2\2\2;\u0132\3\2\2\2=\u0134\3\2\2\2?\u0136\3\2\2\2A\u0138"+
		"\3\2\2\2C\u013a\3\2\2\2E\u013c\3\2\2\2G\u014f\3\2\2\2I\u0152\3\2\2\2K"+
		"\u0165\3\2\2\2M\u0167\3\2\2\2O\u016a\3\2\2\2Q\u016c\3\2\2\2S\u016f\3\2"+
		"\2\2U\u0171\3\2\2\2W\u0174\3\2\2\2Y\u0176\3\2\2\2[\u0179\3\2\2\2]\u017b"+
		"\3\2\2\2_\u017d\3\2\2\2a\u0180\3\2\2\2c\u0184\3\2\2\2e\u0188\3\2\2\2g"+
		"\u018c\3\2\2\2i\u018f\3\2\2\2k\u0192\3\2\2\2m\u0195\3\2\2\2o\u0198\3\2"+
		"\2\2q\u019b\3\2\2\2s\u019d\3\2\2\2u\u019f\3\2\2\2w\u01a1\3\2\2\2y\u01a4"+
		"\3\2\2\2{\u01a7\3\2\2\2}\u01a9\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01ad\3"+
		"\2\2\2\u0083\u01af\3\2\2\2\u0085\u01b3\3\2\2\2\u0087\u01b5\3\2\2\2\u0089"+
		"\u01bf\3\2\2\2\u008b\u01c5\3\2\2\2\u008d\u01c7\3\2\2\2\u008f\u01ca\3\2"+
		"\2\2\u0091\u01d2\3\2\2\2\u0093\u0094\7X\2\2\u0094\u0095\7c\2\2\u0095\u0096"+
		"\7t\2\2\u0096\4\3\2\2\2\u0097\u0098\7H\2\2\u0098\u0099\7w\2\2\u0099\u009a"+
		"\7p\2\2\u009a\u009b\7e\2\2\u009b\u009c\7v\2\2\u009c\u009d\7k\2\2\u009d"+
		"\u009e\7q\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7<\2\2\u00a0\6\3\2\2\2\u00a1"+
		"\u00a2\7D\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7f\2\2\u00a4\u00a5\7{\2\2"+
		"\u00a5\b\3\2\2\2\u00a6\u00a7\7G\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7u"+
		"\2\2\u00a9\u00aa\7g\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\7G\2\2\u00ac\u00ad"+
		"\7p\2\2\u00ad\u00ae\7f\2\2\u00ae\u00af\7H\2\2\u00af\u00b0\7q\2\2\u00b0"+
		"\u00b1\7t\2\2\u00b1\f\3\2\2\2\u00b2\u00b3\7K\2\2\u00b3\u00b4\7h\2\2\u00b4"+
		"\16\3\2\2\2\u00b5\u00b6\7G\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7f\2\2\u00b8"+
		"\u00b9\7F\2\2\u00b9\u00ba\7q\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7D\2\2\u00bc"+
		"\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7c\2\2\u00bf\u00c0\7m\2\2"+
		"\u00c0\22\3\2\2\2\u00c1\u00c2\7G\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7"+
		"u\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7K\2\2\u00c6\u00c7\7h\2\2\u00c7\24"+
		"\3\2\2\2\u00c8\u00c9\7G\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7f\2\2\u00cb"+
		"\u00cc\7Y\2\2\u00cc\u00cd\7j\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7n\2\2"+
		"\u00cf\u00d0\7g\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\7R\2\2\u00d2\u00d3\7"+
		"c\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7o\2\2\u00d6\u00d7"+
		"\7g\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7t\2\2\u00da"+
		"\30\3\2\2\2\u00db\u00dc\7Y\2\2\u00dc\u00dd\7j\2\2\u00dd\u00de\7k\2\2\u00de"+
		"\u00df\7n\2\2\u00df\u00e0\7g\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7E\2\2\u00e2"+
		"\u00e3\7q\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6\7k\2\2"+
		"\u00e6\u00e7\7p\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9\7g\2\2\u00e9\34\3\2"+
		"\2\2\u00ea\u00eb\7G\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7f\2\2\u00ed\u00ee"+
		"\7D\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7f\2\2\u00f0\u00f1\7{\2\2\u00f1"+
		"\u00f2\7\60\2\2\u00f2\36\3\2\2\2\u00f3\u00f4\7H\2\2\u00f4\u00f5\7q\2\2"+
		"\u00f5\u00f6\7t\2\2\u00f6 \3\2\2\2\u00f7\u00f8\7T\2\2\u00f8\u00f9\7g\2"+
		"\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd"+
		"\7p\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7V\2\2\u00ff\u0100\7t\2\2\u0100\u0101"+
		"\7w\2\2\u0101\u0102\7g\2\2\u0102$\3\2\2\2\u0103\u0104\7F\2\2\u0104\u0105"+
		"\7q\2\2\u0105&\3\2\2\2\u0106\u0107\7G\2\2\u0107\u0108\7p\2\2\u0108\u0109"+
		"\7f\2\2\u0109\u010a\7K\2\2\u010a\u010b\7h\2\2\u010b(\3\2\2\2\u010c\u010d"+
		"\7V\2\2\u010d\u010e\7j\2\2\u010e\u010f\7g\2\2\u010f\u0110\7p\2\2\u0110"+
		"*\3\2\2\2\u0111\u0112\7H\2\2\u0112\u0113\7c\2\2\u0113\u0114\7n\2\2\u0114"+
		"\u0115\7u\2\2\u0115\u0116\7g\2\2\u0116,\3\2\2\2\u0117\u0119\t\2\2\2\u0118"+
		"\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3\2"+
		"\2\2\u011b\u011c\3\2\2\2\u011c\u011d\b\27\2\2\u011d.\3\2\2\2\u011e\u0125"+
		"\5}?\2\u011f\u0124\5}?\2\u0120\u0124\5\177@\2\u0121\u0124\5\u0081A\2\u0122"+
		"\u0124\7a\2\2\u0123\u011f\3\2\2\2\u0123\u0120\3\2\2\2\u0123\u0121\3\2"+
		"\2\2\u0123\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125"+
		"\u0126\3\2\2\2\u0126\60\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\7}\2\2"+
		"\u0129\62\3\2\2\2\u012a\u012b\7\177\2\2\u012b\64\3\2\2\2\u012c\u012d\7"+
		"]\2\2\u012d\66\3\2\2\2\u012e\u012f\7_\2\2\u012f8\3\2\2\2\u0130\u0131\7"+
		"*\2\2\u0131:\3\2\2\2\u0132\u0133\7+\2\2\u0133<\3\2\2\2\u0134\u0135\7="+
		"\2\2\u0135>\3\2\2\2\u0136\u0137\7<\2\2\u0137@\3\2\2\2\u0138\u0139\7.\2"+
		"\2\u0139B\3\2\2\2\u013a\u013b\7\60\2\2\u013bD\3\2\2\2\u013c\u013d\7$\2"+
		"\2\u013dF\3\2\2\2\u013e\u0140\5\u0081A\2\u013f\u013e\3\2\2\2\u0140\u0141"+
		"\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0150\3\2\2\2\u0143"+
		"\u0145\5\u0089E\2\u0144\u0146\t\3\2\2\u0145\u0144\3\2\2\2\u0146\u0147"+
		"\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0150\3\2\2\2\u0149"+
		"\u014b\5\u008bF\2\u014a\u014c\t\4\2\2\u014b\u014a\3\2\2\2\u014c\u014d"+
		"\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f"+
		"\u013f\3\2\2\2\u014f\u0143\3\2\2\2\u014f\u0149\3\2\2\2\u0150H\3\2\2\2"+
		"\u0151\u0153\5\u0081A\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154"+
		"\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0161\3\2\2\2\u0156\u015a\5C"+
		"\"\2\u0157\u0159\5\u0081A\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a"+
		"\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3\2"+
		"\2\2\u015d\u015f\5\u0087D\2\u015e\u015d\3\2\2\2\u015e\u015f\3\2\2\2\u015f"+
		"\u0162\3\2\2\2\u0160\u0162\5\u0087D\2\u0161\u0156\3\2\2\2\u0161\u0160"+
		"\3\2\2\2\u0161\u0162\3\2\2\2\u0162J\3\2\2\2\u0163\u0166\5#\22\2\u0164"+
		"\u0166\5+\26\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166L\3\2\2\2"+
		"\u0167\u0168\7-\2\2\u0168\u0169\7\60\2\2\u0169N\3\2\2\2\u016a\u016b\7"+
		"-\2\2\u016bP\3\2\2\2\u016c\u016d\7/\2\2\u016d\u016e\7\60\2\2\u016eR\3"+
		"\2\2\2\u016f\u0170\7/\2\2\u0170T\3\2\2\2\u0171\u0172\7,\2\2\u0172\u0173"+
		"\7\60\2\2\u0173V\3\2\2\2\u0174\u0175\7,\2\2\u0175X\3\2\2\2\u0176\u0177"+
		"\7^\2\2\u0177\u0178\7\60\2\2\u0178Z\3\2\2\2\u0179\u017a\7^\2\2\u017a\\"+
		"\3\2\2\2\u017b\u017c\7\'\2\2\u017c^\3\2\2\2\u017d\u017e\7?\2\2\u017e\u017f"+
		"\7?\2\2\u017f`\3\2\2\2\u0180\u0181\7?\2\2\u0181\u0182\7\61\2\2\u0182\u0183"+
		"\7?\2\2\u0183b\3\2\2\2\u0184\u0185\7>\2\2\u0185\u0186\7?\2\2\u0186\u0187"+
		"\7\60\2\2\u0187d\3\2\2\2\u0188\u0189\7@\2\2\u0189\u018a\7?\2\2\u018a\u018b"+
		"\7\60\2\2\u018bf\3\2\2\2\u018c\u018d\7>\2\2\u018d\u018e\7\60\2\2\u018e"+
		"h\3\2\2\2\u018f\u0190\7@\2\2\u0190\u0191\7\60\2\2\u0191j\3\2\2\2\u0192"+
		"\u0193\7#\2\2\u0193\u0194\7?\2\2\u0194l\3\2\2\2\u0195\u0196\7>\2\2\u0196"+
		"\u0197\7?\2\2\u0197n\3\2\2\2\u0198\u0199\7@\2\2\u0199\u019a\7?\2\2\u019a"+
		"p\3\2\2\2\u019b\u019c\7>\2\2\u019cr\3\2\2\2\u019d\u019e\7@\2\2\u019et"+
		"\3\2\2\2\u019f\u01a0\7#\2\2\u01a0v\3\2\2\2\u01a1\u01a2\7(\2\2\u01a2\u01a3"+
		"\7(\2\2\u01a3x\3\2\2\2\u01a4\u01a5\7~\2\2\u01a5\u01a6\7~\2\2\u01a6z\3"+
		"\2\2\2\u01a7\u01a8\7?\2\2\u01a8|\3\2\2\2\u01a9\u01aa\t\5\2\2\u01aa~\3"+
		"\2\2\2\u01ab\u01ac\t\6\2\2\u01ac\u0080\3\2\2\2\u01ad\u01ae\t\7\2\2\u01ae"+
		"\u0082\3\2\2\2\u01af\u01b0\t\b\2\2\u01b0\u01b1\5\u0085C\2\u01b1\u0084"+
		"\3\2\2\2\u01b2\u01b4\t\t\2\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4"+
		"\u0086\3\2\2\2\u01b5\u01b7\5\u0083B\2\u01b6\u01b8\5\u0081A\2\u01b7\u01b6"+
		"\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba"+
		"\u0088\3\2\2\2\u01bb\u01bc\7\62\2\2\u01bc\u01c0\7z\2\2\u01bd\u01be\7\62"+
		"\2\2\u01be\u01c0\7Z\2\2\u01bf\u01bb\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0"+
		"\u008a\3\2\2\2\u01c1\u01c2\7\62\2\2\u01c2\u01c6\7q\2\2\u01c3\u01c4\7\62"+
		"\2\2\u01c4\u01c6\7Q\2\2\u01c5\u01c1\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6"+
		"\u008c\3\2\2\2\u01c7\u01c8\5\u008fH\2\u01c8\u01c9\5E#\2\u01c9\u008e\3"+
		"\2\2\2\u01ca\u01cb\7)\2\2\u01cb\u0090\3\2\2\2\u01cc\u01cf\5\u008dG\2\u01cd"+
		"\u01cf\n\n\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01ce\u01cf\3\2"+
		"\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2"+
		"\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u0092\3\2\2\2\u01d4\u01d2\3\2"+
		"\2\2\25\2\u011a\u0123\u0125\u0141\u0147\u014d\u014f\u0154\u015a\u015e"+
		"\u0161\u0165\u01b3\u01b9\u01bf\u01c5\u01ce\u01d2\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}