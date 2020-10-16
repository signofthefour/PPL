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
		RETURN=16, TRUE=17, DO=18, ENDIF=19, THEN=20, FALSE=21, WS=22, COMMENT=23, 
		RELATION_OP=24, ADDSUB=25, MULDIV=26, NEGSIGN=27, IDENTIFIER=28, ARRAY=29, 
		LB=30, RB=31, LK=32, RK=33, LP=34, RP=35, SEMI=36, COLON=37, CM=38, DOT=39, 
		DOUQUO=40, INTEGER=41, FLOAT=42, BOLEAN=43, FADDOP=44, IADDOP=45, FSUBOP=46, 
		ISUBOP=47, FMULOP=48, IMULOP=49, FDIVOP=50, IDIVOP=51, IREMAIN=52, EQUAL=53, 
		FNEQUAL=54, FLESSOE=55, FGROE=56, FLESS=57, FGR=58, INEQUAL=59, ILESSOE=60, 
		IGROE=61, ILESS=62, IGR=63, BNEG=64, BAND=65, BOR=66, AS=67, LSTRING=68, 
		STRING=69, NSIGN=70;
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
			"RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "WS", "COMMENT", "RELATION_OP", 
			"ADDSUB", "MULDIV", "NEGSIGN", "IDENTIFIER", "ARRAY", "LB", "RB", "LK", 
			"RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "DOUQUO", "INTEGER", 
			"FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", 
			"IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", 
			"FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", 
			"BNEG", "BAND", "BOR", "AS", "LETTER", "UPCASE_LETTER", "NUMBER", "EXPO", 
			"SIGN", "SCIEN", "HEX", "OCTA", "SDOUQUO", "SINGQUO", "LSTRING", "STRING", 
			"NSIGN"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Var'", "'Function'", "'Body'", "'Else'", "'EndFor'", "'If'", 
			"'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
			"'Continue'", "'EndBody.'", "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", 
			"'Then'", "'False'", null, null, null, null, null, null, null, null, 
			"'{'", "'}'", "'['", "']'", "'('", "')'", "';'", "':'", "','", "'.'", 
			"'\"'", null, null, null, "'+.'", "'+'", "'-.'", "'-'", "'*.'", "'*'", 
			"'\\.'", "'\\'", "'%'", "'=='", "'=/='", "'<=.'", "'>=.'", "'<.'", "'>.'", 
			"'!='", "'<='", "'>='", "'<'", "'>'", "'!'", "'&&'", "'||'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", 
			"ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
			"RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "WS", "COMMENT", "RELATION_OP", 
			"ADDSUB", "MULDIV", "NEGSIGN", "IDENTIFIER", "ARRAY", "LB", "RB", "LK", 
			"RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "DOUQUO", "INTEGER", 
			"FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", 
			"IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", 
			"FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", 
			"BNEG", "BAND", "BOR", "AS", "LSTRING", "STRING", "NSIGN"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2H\u021d\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\27\6\27\u0128\n\27\r\27\16\27\u0129\3\27\3\27\3\30\3\30\3"+
		"\30\3\30\7\30\u0132\n\30\f\30\16\30\u0135\13\30\3\30\3\30\3\30\3\30\3"+
		"\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0147"+
		"\n\31\3\32\3\32\3\32\3\32\5\32\u014d\n\32\3\33\3\33\3\33\3\33\5\33\u0153"+
		"\n\33\3\34\3\34\5\34\u0157\n\34\3\35\3\35\3\35\3\35\3\35\7\35\u015e\n"+
		"\35\f\35\16\35\u0161\13\35\3\36\3\36\3\36\3\36\7\36\u0167\n\36\f\36\16"+
		"\36\u016a\13\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3"+
		"%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\6*\u0185\n*\r*\16*\u0186\3*\3*\6*\u018b"+
		"\n*\r*\16*\u018c\3*\3*\6*\u0191\n*\r*\16*\u0192\5*\u0195\n*\3+\6+\u0198"+
		"\n+\r+\16+\u0199\3+\3+\7+\u019e\n+\f+\16+\u01a1\13+\3+\5+\u01a4\n+\3+"+
		"\5+\u01a7\n+\3,\3,\5,\u01ab\n,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61"+
		"\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66"+
		"\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3"+
		"<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\3E\3E\3"+
		"F\3F\3G\3G\3H\3H\3H\3I\3I\3J\3J\6J\u01fc\nJ\rJ\16J\u01fd\3K\3K\3K\3K\5"+
		"K\u0204\nK\3L\3L\3L\3L\5L\u020a\nL\3M\3M\3M\3N\3N\3O\3O\3O\3O\3P\3P\7"+
		"P\u0217\nP\fP\16P\u021a\13P\3Q\3Q\4\u0133\u0218\2R\3\3\5\4\7\5\t\6\13"+
		"\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'"+
		"\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'"+
		"M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177"+
		"A\u0081B\u0083C\u0085D\u0087E\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2"+
		"\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009dF\u009fG\u00a1H\3\2\13\5"+
		"\2\13\f\17\17\"\"\4\2\62;CH\3\2\629\3\2c|\3\2C\\\3\2\62;\4\2GGgg\4\2-"+
		"-//\3\2$$\2\u0239\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E"+
		"\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2"+
		"\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2"+
		"\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k"+
		"\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2"+
		"\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2"+
		"\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u009d\3\2\2\2\2\u009f"+
		"\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3\3\2\2\2\5\u00a7\3\2\2\2\7\u00b0\3\2\2"+
		"\2\t\u00b5\3\2\2\2\13\u00ba\3\2\2\2\r\u00c1\3\2\2\2\17\u00c4\3\2\2\2\21"+
		"\u00ca\3\2\2\2\23\u00d0\3\2\2\2\25\u00d7\3\2\2\2\27\u00e0\3\2\2\2\31\u00ea"+
		"\3\2\2\2\33\u00f0\3\2\2\2\35\u00f9\3\2\2\2\37\u0102\3\2\2\2!\u0106\3\2"+
		"\2\2#\u010d\3\2\2\2%\u0112\3\2\2\2\'\u0115\3\2\2\2)\u011b\3\2\2\2+\u0120"+
		"\3\2\2\2-\u0127\3\2\2\2/\u012d\3\2\2\2\61\u0146\3\2\2\2\63\u014c\3\2\2"+
		"\2\65\u0152\3\2\2\2\67\u0156\3\2\2\29\u0158\3\2\2\2;\u0162\3\2\2\2=\u016d"+
		"\3\2\2\2?\u016f\3\2\2\2A\u0171\3\2\2\2C\u0173\3\2\2\2E\u0175\3\2\2\2G"+
		"\u0177\3\2\2\2I\u0179\3\2\2\2K\u017b\3\2\2\2M\u017d\3\2\2\2O\u017f\3\2"+
		"\2\2Q\u0181\3\2\2\2S\u0194\3\2\2\2U\u0197\3\2\2\2W\u01aa\3\2\2\2Y\u01ac"+
		"\3\2\2\2[\u01af\3\2\2\2]\u01b1\3\2\2\2_\u01b4\3\2\2\2a\u01b6\3\2\2\2c"+
		"\u01b9\3\2\2\2e\u01bb\3\2\2\2g\u01be\3\2\2\2i\u01c0\3\2\2\2k\u01c2\3\2"+
		"\2\2m\u01c5\3\2\2\2o\u01c9\3\2\2\2q\u01cd\3\2\2\2s\u01d1\3\2\2\2u\u01d4"+
		"\3\2\2\2w\u01d7\3\2\2\2y\u01da\3\2\2\2{\u01dd\3\2\2\2}\u01e0\3\2\2\2\177"+
		"\u01e2\3\2\2\2\u0081\u01e4\3\2\2\2\u0083\u01e6\3\2\2\2\u0085\u01e9\3\2"+
		"\2\2\u0087\u01ec\3\2\2\2\u0089\u01ee\3\2\2\2\u008b\u01f0\3\2\2\2\u008d"+
		"\u01f2\3\2\2\2\u008f\u01f4\3\2\2\2\u0091\u01f7\3\2\2\2\u0093\u01f9\3\2"+
		"\2\2\u0095\u0203\3\2\2\2\u0097\u0209\3\2\2\2\u0099\u020b\3\2\2\2\u009b"+
		"\u020e\3\2\2\2\u009d\u0210\3\2\2\2\u009f\u0218\3\2\2\2\u00a1\u021b\3\2"+
		"\2\2\u00a3\u00a4\7X\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7t\2\2\u00a6\4"+
		"\3\2\2\2\u00a7\u00a8\7H\2\2\u00a8\u00a9\7w\2\2\u00a9\u00aa\7p\2\2\u00aa"+
		"\u00ab\7e\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7q\2\2"+
		"\u00ae\u00af\7p\2\2\u00af\6\3\2\2\2\u00b0\u00b1\7D\2\2\u00b1\u00b2\7q"+
		"\2\2\u00b2\u00b3\7f\2\2\u00b3\u00b4\7{\2\2\u00b4\b\3\2\2\2\u00b5\u00b6"+
		"\7G\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9\7g\2\2\u00b9"+
		"\n\3\2\2\2\u00ba\u00bb\7G\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7f\2\2\u00bd"+
		"\u00be\7H\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0\7t\2\2\u00c0\f\3\2\2\2\u00c1"+
		"\u00c2\7K\2\2\u00c2\u00c3\7h\2\2\u00c3\16\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5"+
		"\u00c6\7p\2\2\u00c6\u00c7\7f\2\2\u00c7\u00c8\7F\2\2\u00c8\u00c9\7q\2\2"+
		"\u00c9\20\3\2\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7"+
		"g\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7m\2\2\u00cf\22\3\2\2\2\u00d0\u00d1"+
		"\7G\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4\7g\2\2\u00d4"+
		"\u00d5\7K\2\2\u00d5\u00d6\7h\2\2\u00d6\24\3\2\2\2\u00d7\u00d8\7G\2\2\u00d8"+
		"\u00d9\7p\2\2\u00d9\u00da\7f\2\2\u00da\u00db\7Y\2\2\u00db\u00dc\7j\2\2"+
		"\u00dc\u00dd\7k\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7g\2\2\u00df\26\3\2"+
		"\2\2\u00e0\u00e1\7R\2\2\u00e1\u00e2\7c\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4"+
		"\7c\2\2\u00e4\u00e5\7o\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7v\2\2\u00e7"+
		"\u00e8\7g\2\2\u00e8\u00e9\7t\2\2\u00e9\30\3\2\2\2\u00ea\u00eb\7Y\2\2\u00eb"+
		"\u00ec\7j\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef\7g\2\2"+
		"\u00ef\32\3\2\2\2\u00f0\u00f1\7E\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7"+
		"p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7"+
		"\7w\2\2\u00f7\u00f8\7g\2\2\u00f8\34\3\2\2\2\u00f9\u00fa\7G\2\2\u00fa\u00fb"+
		"\7p\2\2\u00fb\u00fc\7f\2\2\u00fc\u00fd\7D\2\2\u00fd\u00fe\7q\2\2\u00fe"+
		"\u00ff\7f\2\2\u00ff\u0100\7{\2\2\u0100\u0101\7\60\2\2\u0101\36\3\2\2\2"+
		"\u0102\u0103\7H\2\2\u0103\u0104\7q\2\2\u0104\u0105\7t\2\2\u0105 \3\2\2"+
		"\2\u0106\u0107\7T\2\2\u0107\u0108\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a"+
		"\7w\2\2\u010a\u010b\7t\2\2\u010b\u010c\7p\2\2\u010c\"\3\2\2\2\u010d\u010e"+
		"\7V\2\2\u010e\u010f\7t\2\2\u010f\u0110\7w\2\2\u0110\u0111\7g\2\2\u0111"+
		"$\3\2\2\2\u0112\u0113\7F\2\2\u0113\u0114\7q\2\2\u0114&\3\2\2\2\u0115\u0116"+
		"\7G\2\2\u0116\u0117\7p\2\2\u0117\u0118\7f\2\2\u0118\u0119\7K\2\2\u0119"+
		"\u011a\7h\2\2\u011a(\3\2\2\2\u011b\u011c\7V\2\2\u011c\u011d\7j\2\2\u011d"+
		"\u011e\7g\2\2\u011e\u011f\7p\2\2\u011f*\3\2\2\2\u0120\u0121\7H\2\2\u0121"+
		"\u0122\7c\2\2\u0122\u0123\7n\2\2\u0123\u0124\7u\2\2\u0124\u0125\7g\2\2"+
		"\u0125,\3\2\2\2\u0126\u0128\t\2\2\2\u0127\u0126\3\2\2\2\u0128\u0129\3"+
		"\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b"+
		"\u012c\b\27\2\2\u012c.\3\2\2\2\u012d\u012e\7,\2\2\u012e\u012f\7,\2\2\u012f"+
		"\u0133\3\2\2\2\u0130\u0132\13\2\2\2\u0131\u0130\3\2\2\2\u0132\u0135\3"+
		"\2\2\2\u0133\u0134\3\2\2\2\u0133\u0131\3\2\2\2\u0134\u0136\3\2\2\2\u0135"+
		"\u0133\3\2\2\2\u0136\u0137\7,\2\2\u0137\u0138\7,\2\2\u0138\u0139\3\2\2"+
		"\2\u0139\u013a\b\30\2\2\u013a\60\3\2\2\2\u013b\u0147\5k\66\2\u013c\u0147"+
		"\5m\67\2\u013d\u0147\5o8\2\u013e\u0147\5q9\2\u013f\u0147\5s:\2\u0140\u0147"+
		"\5u;\2\u0141\u0147\5w<\2\u0142\u0147\5y=\2\u0143\u0147\5{>\2\u0144\u0147"+
		"\5}?\2\u0145\u0147\5\177@\2\u0146\u013b\3\2\2\2\u0146\u013c\3\2\2\2\u0146"+
		"\u013d\3\2\2\2\u0146\u013e\3\2\2\2\u0146\u013f\3\2\2\2\u0146\u0140\3\2"+
		"\2\2\u0146\u0141\3\2\2\2\u0146\u0142\3\2\2\2\u0146\u0143\3\2\2\2\u0146"+
		"\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147\62\3\2\2\2\u0148\u014d\5Y-\2"+
		"\u0149\u014d\5]/\2\u014a\u014d\5[.\2\u014b\u014d\5_\60\2\u014c\u0148\3"+
		"\2\2\2\u014c\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d"+
		"\64\3\2\2\2\u014e\u0153\5a\61\2\u014f\u0153\5e\63\2\u0150\u0153\5c\62"+
		"\2\u0151\u0153\5g\64\2\u0152\u014e\3\2\2\2\u0152\u014f\3\2\2\2\u0152\u0150"+
		"\3\2\2\2\u0152\u0151\3\2\2\2\u0153\66\3\2\2\2\u0154\u0157\5_\60\2\u0155"+
		"\u0157\5]/\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u01578\3\2\2\2\u0158"+
		"\u015f\5\u0089E\2\u0159\u015e\5\u0089E\2\u015a\u015e\5\u008bF\2\u015b"+
		"\u015e\5\u008dG\2\u015c\u015e\7a\2\2\u015d\u0159\3\2\2\2\u015d\u015a\3"+
		"\2\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f"+
		"\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160:\3\2\2\2\u0161\u015f\3\2\2\2"+
		"\u0162\u0163\5=\37\2\u0163\u0168\5\u008dG\2\u0164\u0165\7.\2\2\u0165\u0167"+
		"\5\u008dG\2\u0166\u0164\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2"+
		"\2\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c"+
		"\5? \2\u016c<\3\2\2\2\u016d\u016e\7}\2\2\u016e>\3\2\2\2\u016f\u0170\7"+
		"\177\2\2\u0170@\3\2\2\2\u0171\u0172\7]\2\2\u0172B\3\2\2\2\u0173\u0174"+
		"\7_\2\2\u0174D\3\2\2\2\u0175\u0176\7*\2\2\u0176F\3\2\2\2\u0177\u0178\7"+
		"+\2\2\u0178H\3\2\2\2\u0179\u017a\7=\2\2\u017aJ\3\2\2\2\u017b\u017c\7<"+
		"\2\2\u017cL\3\2\2\2\u017d\u017e\7.\2\2\u017eN\3\2\2\2\u017f\u0180\7\60"+
		"\2\2\u0180P\3\2\2\2\u0181\u0182\7$\2\2\u0182R\3\2\2\2\u0183\u0185\5\u008d"+
		"G\2\u0184\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186"+
		"\u0187\3\2\2\2\u0187\u0195\3\2\2\2\u0188\u018a\5\u0095K\2\u0189\u018b"+
		"\t\3\2\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c"+
		"\u018d\3\2\2\2\u018d\u0195\3\2\2\2\u018e\u0190\5\u0097L\2\u018f\u0191"+
		"\t\4\2\2\u0190\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0190\3\2\2\2\u0192"+
		"\u0193\3\2\2\2\u0193\u0195\3\2\2\2\u0194\u0184\3\2\2\2\u0194\u0188\3\2"+
		"\2\2\u0194\u018e\3\2\2\2\u0195T\3\2\2\2\u0196\u0198\5\u008dG\2\u0197\u0196"+
		"\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a"+
		"\u01a6\3\2\2\2\u019b\u019f\5O(\2\u019c\u019e\5\u008dG\2\u019d\u019c\3"+
		"\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0"+
		"\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a4\5\u0093J\2\u01a3\u01a2"+
		"\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5\u01a7\5\u0093J"+
		"\2\u01a6\u019b\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7V\3\2\2\2\u01a8\u01ab"+
		"\5#\22\2\u01a9\u01ab\5+\26\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab"+
		"X\3\2\2\2\u01ac\u01ad\7-\2\2\u01ad\u01ae\7\60\2\2\u01aeZ\3\2\2\2\u01af"+
		"\u01b0\7-\2\2\u01b0\\\3\2\2\2\u01b1\u01b2\7/\2\2\u01b2\u01b3\7\60\2\2"+
		"\u01b3^\3\2\2\2\u01b4\u01b5\7/\2\2\u01b5`\3\2\2\2\u01b6\u01b7\7,\2\2\u01b7"+
		"\u01b8\7\60\2\2\u01b8b\3\2\2\2\u01b9\u01ba\7,\2\2\u01bad\3\2\2\2\u01bb"+
		"\u01bc\7^\2\2\u01bc\u01bd\7\60\2\2\u01bdf\3\2\2\2\u01be\u01bf\7^\2\2\u01bf"+
		"h\3\2\2\2\u01c0\u01c1\7\'\2\2\u01c1j\3\2\2\2\u01c2\u01c3\7?\2\2\u01c3"+
		"\u01c4\7?\2\2\u01c4l\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6\u01c7\7\61\2\2\u01c7"+
		"\u01c8\7?\2\2\u01c8n\3\2\2\2\u01c9\u01ca\7>\2\2\u01ca\u01cb\7?\2\2\u01cb"+
		"\u01cc\7\60\2\2\u01ccp\3\2\2\2\u01cd\u01ce\7@\2\2\u01ce\u01cf\7?\2\2\u01cf"+
		"\u01d0\7\60\2\2\u01d0r\3\2\2\2\u01d1\u01d2\7>\2\2\u01d2\u01d3\7\60\2\2"+
		"\u01d3t\3\2\2\2\u01d4\u01d5\7@\2\2\u01d5\u01d6\7\60\2\2\u01d6v\3\2\2\2"+
		"\u01d7\u01d8\7#\2\2\u01d8\u01d9\7?\2\2\u01d9x\3\2\2\2\u01da\u01db\7>\2"+
		"\2\u01db\u01dc\7?\2\2\u01dcz\3\2\2\2\u01dd\u01de\7@\2\2\u01de\u01df\7"+
		"?\2\2\u01df|\3\2\2\2\u01e0\u01e1\7>\2\2\u01e1~\3\2\2\2\u01e2\u01e3\7@"+
		"\2\2\u01e3\u0080\3\2\2\2\u01e4\u01e5\7#\2\2\u01e5\u0082\3\2\2\2\u01e6"+
		"\u01e7\7(\2\2\u01e7\u01e8\7(\2\2\u01e8\u0084\3\2\2\2\u01e9\u01ea\7~\2"+
		"\2\u01ea\u01eb\7~\2\2\u01eb\u0086\3\2\2\2\u01ec\u01ed\7?\2\2\u01ed\u0088"+
		"\3\2\2\2\u01ee\u01ef\t\5\2\2\u01ef\u008a\3\2\2\2\u01f0\u01f1\t\6\2\2\u01f1"+
		"\u008c\3\2\2\2\u01f2\u01f3\t\7\2\2\u01f3\u008e\3\2\2\2\u01f4\u01f5\t\b"+
		"\2\2\u01f5\u01f6\5\u0091I\2\u01f6\u0090\3\2\2\2\u01f7\u01f8\t\t\2\2\u01f8"+
		"\u0092\3\2\2\2\u01f9\u01fb\5\u008fH\2\u01fa\u01fc\5\u008dG\2\u01fb\u01fa"+
		"\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe"+
		"\u0094\3\2\2\2\u01ff\u0200\7\62\2\2\u0200\u0204\7z\2\2\u0201\u0202\7\62"+
		"\2\2\u0202\u0204\7Z\2\2\u0203\u01ff\3\2\2\2\u0203\u0201\3\2\2\2\u0204"+
		"\u0096\3\2\2\2\u0205\u0206\7\62\2\2\u0206\u020a\7q\2\2\u0207\u0208\7\62"+
		"\2\2\u0208\u020a\7Q\2\2\u0209\u0205\3\2\2\2\u0209\u0207\3\2\2\2\u020a"+
		"\u0098\3\2\2\2\u020b\u020c\5\u009bN\2\u020c\u020d\5Q)\2\u020d\u009a\3"+
		"\2\2\2\u020e\u020f\7)\2\2\u020f\u009c\3\2\2\2\u0210\u0211\5Q)\2\u0211"+
		"\u0212\5\u009fP\2\u0212\u0213\5Q)\2\u0213\u009e\3\2\2\2\u0214\u0217\5"+
		"\u0099M\2\u0215\u0217\n\n\2\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2\2\2"+
		"\u0217\u021a\3\2\2\2\u0218\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219\u00a0"+
		"\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\5\u0091I\2\u021c\u00a2\3\2\2"+
		"\2\32\2\u0129\u0133\u0146\u014c\u0152\u0156\u015d\u015f\u0168\u0186\u018c"+
		"\u0192\u0194\u0199\u019f\u01a3\u01a6\u01aa\u01fd\u0203\u0209\u0216\u0218"+
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