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
		INTEGER=34, FLOAT=35, BOLEAN=36, FADDOP=37, IADDOP=38, FSUBOP=39, ISUBOP=40, 
		FMULOP=41, IMULOP=42, FDIVOP=43, IDIVOP=44, IREMAIN=45, EQUAL=46, FNEQUAL=47, 
		FLESSOE=48, FGROE=49, FLESS=50, FGR=51, INEQUAL=52, ILESSOE=53, IGROE=54, 
		ILESS=55, IGR=56, BNEG=57, BAND=58, BOR=59, AS=60;
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
			"FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", 
			"IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", 
			"FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", 
			"BNEG", "BAND", "BOR", "AS", "LETTER", "UPCASE_LETTER", "NUMBER", "EXPO", 
			"SIGN", "SCIEN", "HEX", "OCTA"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Var'", "'Function:'", "'Body'", "'Else'", "'EndFor'", "'If'", 
			"'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", "'While'", 
			"'Continue'", "'EndBody.'", "'For'", "'Return'", "'True'", "'Do'", "'EndIf'", 
			"'Then'", "'False'", null, null, "'{'", "'}'", "'['", "']'", "'('", "')'", 
			"';'", "':'", "','", "'.'", null, null, null, "'+.'", "'+'", "'-.'", 
			"'-'", "'*.'", "'*'", "'\\.'", "'\\'", "'%'", "'=='", "'=/='", "'<=.'", 
			"'>=.'", "'<.'", "'>.'", "'!='", "'<='", "'>='", "'<'", "'>'", "'!'", 
			"'&&'", "'||'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", "ENDDO", "BREAK", 
			"ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", "ENDBODY", "FOR", 
			"RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "WS", "IDENTIFIER", 
			"LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "INTEGER", 
			"FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", 
			"IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", 
			"FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", 
			"BNEG", "BAND", "BOR", "AS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>\u01bd\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5"+
		"\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\27\6\27\u0111\n\27\r\27\16\27\u0112\3\27\3\27\3\30\3\30\3"+
		"\30\3\30\3\30\7\30\u011c\n\30\f\30\16\30\u011f\13\30\3\31\3\31\3\32\3"+
		"\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\""+
		"\3\"\3#\6#\u0136\n#\r#\16#\u0137\3#\3#\6#\u013c\n#\r#\16#\u013d\3#\3#"+
		"\6#\u0142\n#\r#\16#\u0143\5#\u0146\n#\3$\6$\u0149\n$\r$\16$\u014a\3$\3"+
		"$\7$\u014f\n$\f$\16$\u0152\13$\3$\5$\u0155\n$\3$\5$\u0158\n$\3%\3%\5%"+
		"\u015c\n%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3"+
		"-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62"+
		"\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67"+
		"\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3"+
		"@\3A\3A\3A\3B\5B\u01aa\nB\3C\3C\6C\u01ae\nC\rC\16C\u01af\3D\3D\3D\3D\5"+
		"D\u01b6\nD\3E\3E\3E\3E\5E\u01bc\nE\2\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t"+
		"\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27"+
		"-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W"+
		"-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{\2}\2\177\2\u0081"+
		"\2\u0083\2\u0085\2\u0087\2\u0089\2\3\2\n\5\2\13\f\17\17\"\"\4\2\62;CH"+
		"\3\2\629\3\2c|\3\2C\\\3\2\62;\4\2GGgg\4\2--//\2\u01c8\2\3\3\2\2\2\2\5"+
		"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2"+
		"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33"+
		"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2"+
		"\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2"+
		"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2"+
		"\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K"+
		"\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2"+
		"\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2"+
		"\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q"+
		"\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3\u008b\3\2\2\2\5"+
		"\u008f\3\2\2\2\7\u0099\3\2\2\2\t\u009e\3\2\2\2\13\u00a3\3\2\2\2\r\u00aa"+
		"\3\2\2\2\17\u00ad\3\2\2\2\21\u00b3\3\2\2\2\23\u00b9\3\2\2\2\25\u00c0\3"+
		"\2\2\2\27\u00c9\3\2\2\2\31\u00d3\3\2\2\2\33\u00d9\3\2\2\2\35\u00e2\3\2"+
		"\2\2\37\u00eb\3\2\2\2!\u00ef\3\2\2\2#\u00f6\3\2\2\2%\u00fb\3\2\2\2\'\u00fe"+
		"\3\2\2\2)\u0104\3\2\2\2+\u0109\3\2\2\2-\u0110\3\2\2\2/\u0116\3\2\2\2\61"+
		"\u0120\3\2\2\2\63\u0122\3\2\2\2\65\u0124\3\2\2\2\67\u0126\3\2\2\29\u0128"+
		"\3\2\2\2;\u012a\3\2\2\2=\u012c\3\2\2\2?\u012e\3\2\2\2A\u0130\3\2\2\2C"+
		"\u0132\3\2\2\2E\u0145\3\2\2\2G\u0148\3\2\2\2I\u015b\3\2\2\2K\u015d\3\2"+
		"\2\2M\u0160\3\2\2\2O\u0162\3\2\2\2Q\u0165\3\2\2\2S\u0167\3\2\2\2U\u016a"+
		"\3\2\2\2W\u016c\3\2\2\2Y\u016f\3\2\2\2[\u0171\3\2\2\2]\u0173\3\2\2\2_"+
		"\u0176\3\2\2\2a\u017a\3\2\2\2c\u017e\3\2\2\2e\u0182\3\2\2\2g\u0185\3\2"+
		"\2\2i\u0188\3\2\2\2k\u018b\3\2\2\2m\u018e\3\2\2\2o\u0191\3\2\2\2q\u0193"+
		"\3\2\2\2s\u0195\3\2\2\2u\u0197\3\2\2\2w\u019a\3\2\2\2y\u019d\3\2\2\2{"+
		"\u019f\3\2\2\2}\u01a1\3\2\2\2\177\u01a3\3\2\2\2\u0081\u01a5\3\2\2\2\u0083"+
		"\u01a9\3\2\2\2\u0085\u01ab\3\2\2\2\u0087\u01b5\3\2\2\2\u0089\u01bb\3\2"+
		"\2\2\u008b\u008c\7X\2\2\u008c\u008d\7c\2\2\u008d\u008e\7t\2\2\u008e\4"+
		"\3\2\2\2\u008f\u0090\7H\2\2\u0090\u0091\7w\2\2\u0091\u0092\7p\2\2\u0092"+
		"\u0093\7e\2\2\u0093\u0094\7v\2\2\u0094\u0095\7k\2\2\u0095\u0096\7q\2\2"+
		"\u0096\u0097\7p\2\2\u0097\u0098\7<\2\2\u0098\6\3\2\2\2\u0099\u009a\7D"+
		"\2\2\u009a\u009b\7q\2\2\u009b\u009c\7f\2\2\u009c\u009d\7{\2\2\u009d\b"+
		"\3\2\2\2\u009e\u009f\7G\2\2\u009f\u00a0\7n\2\2\u00a0\u00a1\7u\2\2\u00a1"+
		"\u00a2\7g\2\2\u00a2\n\3\2\2\2\u00a3\u00a4\7G\2\2\u00a4\u00a5\7p\2\2\u00a5"+
		"\u00a6\7f\2\2\u00a6\u00a7\7H\2\2\u00a7\u00a8\7q\2\2\u00a8\u00a9\7t\2\2"+
		"\u00a9\f\3\2\2\2\u00aa\u00ab\7K\2\2\u00ab\u00ac\7h\2\2\u00ac\16\3\2\2"+
		"\2\u00ad\u00ae\7G\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7f\2\2\u00b0\u00b1"+
		"\7F\2\2\u00b1\u00b2\7q\2\2\u00b2\20\3\2\2\2\u00b3\u00b4\7D\2\2\u00b4\u00b5"+
		"\7t\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7m\2\2\u00b8"+
		"\22\3\2\2\2\u00b9\u00ba\7G\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7u\2\2\u00bc"+
		"\u00bd\7g\2\2\u00bd\u00be\7K\2\2\u00be\u00bf\7h\2\2\u00bf\24\3\2\2\2\u00c0"+
		"\u00c1\7G\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4\7Y\2\2"+
		"\u00c4\u00c5\7j\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8"+
		"\7g\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\7R\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc"+
		"\7t\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7o\2\2\u00ce\u00cf\7g\2\2\u00cf"+
		"\u00d0\7v\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7t\2\2\u00d2\30\3\2\2\2\u00d3"+
		"\u00d4\7Y\2\2\u00d4\u00d5\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7n\2\2"+
		"\u00d7\u00d8\7g\2\2\u00d8\32\3\2\2\2\u00d9\u00da\7E\2\2\u00da\u00db\7"+
		"q\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd\7v\2\2\u00dd\u00de\7k\2\2\u00de\u00df"+
		"\7p\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1\7g\2\2\u00e1\34\3\2\2\2\u00e2\u00e3"+
		"\7G\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7f\2\2\u00e5\u00e6\7D\2\2\u00e6"+
		"\u00e7\7q\2\2\u00e7\u00e8\7f\2\2\u00e8\u00e9\7{\2\2\u00e9\u00ea\7\60\2"+
		"\2\u00ea\36\3\2\2\2\u00eb\u00ec\7H\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee"+
		"\7t\2\2\u00ee \3\2\2\2\u00ef\u00f0\7T\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2"+
		"\7v\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7p\2\2\u00f5"+
		"\"\3\2\2\2\u00f6\u00f7\7V\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7w\2\2\u00f9"+
		"\u00fa\7g\2\2\u00fa$\3\2\2\2\u00fb\u00fc\7F\2\2\u00fc\u00fd\7q\2\2\u00fd"+
		"&\3\2\2\2\u00fe\u00ff\7G\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7f\2\2\u0101"+
		"\u0102\7K\2\2\u0102\u0103\7h\2\2\u0103(\3\2\2\2\u0104\u0105\7V\2\2\u0105"+
		"\u0106\7j\2\2\u0106\u0107\7g\2\2\u0107\u0108\7p\2\2\u0108*\3\2\2\2\u0109"+
		"\u010a\7H\2\2\u010a\u010b\7c\2\2\u010b\u010c\7n\2\2\u010c\u010d\7u\2\2"+
		"\u010d\u010e\7g\2\2\u010e,\3\2\2\2\u010f\u0111\t\2\2\2\u0110\u010f\3\2"+
		"\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113"+
		"\u0114\3\2\2\2\u0114\u0115\b\27\2\2\u0115.\3\2\2\2\u0116\u011d\5{>\2\u0117"+
		"\u011c\5{>\2\u0118\u011c\5}?\2\u0119\u011c\5\177@\2\u011a\u011c\7a\2\2"+
		"\u011b\u0117\3\2\2\2\u011b\u0118\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011a"+
		"\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e"+
		"\60\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7}\2\2\u0121\62\3\2\2\2\u0122"+
		"\u0123\7\177\2\2\u0123\64\3\2\2\2\u0124\u0125\7]\2\2\u0125\66\3\2\2\2"+
		"\u0126\u0127\7_\2\2\u01278\3\2\2\2\u0128\u0129\7*\2\2\u0129:\3\2\2\2\u012a"+
		"\u012b\7+\2\2\u012b<\3\2\2\2\u012c\u012d\7=\2\2\u012d>\3\2\2\2\u012e\u012f"+
		"\7<\2\2\u012f@\3\2\2\2\u0130\u0131\7.\2\2\u0131B\3\2\2\2\u0132\u0133\7"+
		"\60\2\2\u0133D\3\2\2\2\u0134\u0136\5\177@\2\u0135\u0134\3\2\2\2\u0136"+
		"\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u0146\3\2"+
		"\2\2\u0139\u013b\5\u0087D\2\u013a\u013c\t\3\2\2\u013b\u013a\3\2\2\2\u013c"+
		"\u013d\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0146\3\2"+
		"\2\2\u013f\u0141\5\u0089E\2\u0140\u0142\t\4\2\2\u0141\u0140\3\2\2\2\u0142"+
		"\u0143\3\2\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2"+
		"\2\2\u0145\u0135\3\2\2\2\u0145\u0139\3\2\2\2\u0145\u013f\3\2\2\2\u0146"+
		"F\3\2\2\2\u0147\u0149\5\177@\2\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2"+
		"\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u0157\3\2\2\2\u014c\u0150"+
		"\5C\"\2\u014d\u014f\5\177@\2\u014e\u014d\3\2\2\2\u014f\u0152\3\2\2\2\u0150"+
		"\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2"+
		"\2\2\u0153\u0155\5\u0085C\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155"+
		"\u0158\3\2\2\2\u0156\u0158\5\u0085C\2\u0157\u014c\3\2\2\2\u0157\u0156"+
		"\3\2\2\2\u0157\u0158\3\2\2\2\u0158H\3\2\2\2\u0159\u015c\5#\22\2\u015a"+
		"\u015c\5+\26\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2\u015cJ\3\2\2\2"+
		"\u015d\u015e\7-\2\2\u015e\u015f\7\60\2\2\u015fL\3\2\2\2\u0160\u0161\7"+
		"-\2\2\u0161N\3\2\2\2\u0162\u0163\7/\2\2\u0163\u0164\7\60\2\2\u0164P\3"+
		"\2\2\2\u0165\u0166\7/\2\2\u0166R\3\2\2\2\u0167\u0168\7,\2\2\u0168\u0169"+
		"\7\60\2\2\u0169T\3\2\2\2\u016a\u016b\7,\2\2\u016bV\3\2\2\2\u016c\u016d"+
		"\7^\2\2\u016d\u016e\7\60\2\2\u016eX\3\2\2\2\u016f\u0170\7^\2\2\u0170Z"+
		"\3\2\2\2\u0171\u0172\7\'\2\2\u0172\\\3\2\2\2\u0173\u0174\7?\2\2\u0174"+
		"\u0175\7?\2\2\u0175^\3\2\2\2\u0176\u0177\7?\2\2\u0177\u0178\7\61\2\2\u0178"+
		"\u0179\7?\2\2\u0179`\3\2\2\2\u017a\u017b\7>\2\2\u017b\u017c\7?\2\2\u017c"+
		"\u017d\7\60\2\2\u017db\3\2\2\2\u017e\u017f\7@\2\2\u017f\u0180\7?\2\2\u0180"+
		"\u0181\7\60\2\2\u0181d\3\2\2\2\u0182\u0183\7>\2\2\u0183\u0184\7\60\2\2"+
		"\u0184f\3\2\2\2\u0185\u0186\7@\2\2\u0186\u0187\7\60\2\2\u0187h\3\2\2\2"+
		"\u0188\u0189\7#\2\2\u0189\u018a\7?\2\2\u018aj\3\2\2\2\u018b\u018c\7>\2"+
		"\2\u018c\u018d\7?\2\2\u018dl\3\2\2\2\u018e\u018f\7@\2\2\u018f\u0190\7"+
		"?\2\2\u0190n\3\2\2\2\u0191\u0192\7>\2\2\u0192p\3\2\2\2\u0193\u0194\7@"+
		"\2\2\u0194r\3\2\2\2\u0195\u0196\7#\2\2\u0196t\3\2\2\2\u0197\u0198\7(\2"+
		"\2\u0198\u0199\7(\2\2\u0199v\3\2\2\2\u019a\u019b\7~\2\2\u019b\u019c\7"+
		"~\2\2\u019cx\3\2\2\2\u019d\u019e\7?\2\2\u019ez\3\2\2\2\u019f\u01a0\t\5"+
		"\2\2\u01a0|\3\2\2\2\u01a1\u01a2\t\6\2\2\u01a2~\3\2\2\2\u01a3\u01a4\t\7"+
		"\2\2\u01a4\u0080\3\2\2\2\u01a5\u01a6\t\b\2\2\u01a6\u01a7\5\u0083B\2\u01a7"+
		"\u0082\3\2\2\2\u01a8\u01aa\t\t\2\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2"+
		"\2\2\u01aa\u0084\3\2\2\2\u01ab\u01ad\5\u0081A\2\u01ac\u01ae\5\177@\2\u01ad"+
		"\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01ad\3\2\2\2\u01af\u01b0\3\2"+
		"\2\2\u01b0\u0086\3\2\2\2\u01b1\u01b2\7\62\2\2\u01b2\u01b6\7z\2\2\u01b3"+
		"\u01b4\7\62\2\2\u01b4\u01b6\7Z\2\2\u01b5\u01b1\3\2\2\2\u01b5\u01b3\3\2"+
		"\2\2\u01b6\u0088\3\2\2\2\u01b7\u01b8\7\62\2\2\u01b8\u01bc\7q\2\2\u01b9"+
		"\u01ba\7\62\2\2\u01ba\u01bc\7Q\2\2\u01bb\u01b7\3\2\2\2\u01bb\u01b9\3\2"+
		"\2\2\u01bc\u008a\3\2\2\2\23\2\u0112\u011b\u011d\u0137\u013d\u0143\u0145"+
		"\u014a\u0150\u0154\u0157\u015b\u01a9\u01af\u01b5\u01bb\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}