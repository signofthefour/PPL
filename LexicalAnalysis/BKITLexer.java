// Generated from BKIT.g4 by ANTLR 4.8
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
		REAL_NUMBER=1, ID=2, ILLEGAL_ESCAPE=3, UNCLOSE_STRING=4, COMMENT=5, UNTERMINATED_COMMENT=6, 
		ERROR_CHAR=7, WS=8, Integer_literal=9, Float_literal=10, Boolean_literal=11, 
		String_literal=12, BODY=13, BREAK=14, CONTINUE=15, DO=16, ELSE=17, ELSELF=18, 
		ELSEIF=19, ENDBODY=20, ENDFOR=21, ENDWHILE=22, FOR=23, FUNCTION=24, IF=25, 
		PARAMETER=26, RETURN=27, THEN=28, VAR=29, WHILE=30, TRUE=31, FALSE=32, 
		ENDDO=33, PLUS_INT=34, PLUS_FLOAT=35, MINUS_INT=36, MINUS_FLOAT=37, STAR_INT=38, 
		STAR_FLOAT=39, DIV_INT=40, DIV_FLOAT=41, MOD=42, NOT=43, AND=44, OR=45, 
		EQUAL=46, NOT_EQUAL_INT=47, LESS_INT=48, GREATER_INT=49, LESS_OR_EQUAL_INT=50, 
		GREATER_OR_EQUAL_INT=51, NOT_EQUAL_FLOAT=52, LESS_FLOAT=53, GREATER_FLOAT=54, 
		LESS_OR_EQUAL_FLOAT=55, GREATER_OR_EQUAL_FLOAT=56, LEFT_PAREN=57, RIGHT_PARENT=58, 
		LEFT_BRACKET=59, RIGHT_BRACKET=60, LEFT_BRACE=61, RIGHT_BRACE=62, COLON=63, 
		DOT=64, SEMI=65, COMMA=66;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"REAL_NUMBER", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", "UNTERMINATED_COMMENT", 
			"ERROR_CHAR", "WS", "LOWERCASE_LETTER", "UPPERCASE_LETTER", "DIGIT", 
			"LETTER", "SIGN", "SCIENTIFIC", "DECIMAL_POINT", "FLOATING_POINT_NUM", 
			"ILL_ESC_SEQUENCE", "SUP_ESC_SEQUENCE", "DOUBLE_QUOTE_IN_STRING", "STRING_CHAR", 
			"HEXADECIMALDIGIT", "OCTALDIGIT", "HEXADECIMAL", "DECIMAL", "OCTAL", 
			"DOUBLE_QUOTE", "Integer_literal", "Float_literal", "Boolean_literal", 
			"String_literal", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSELF", 
			"ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
			"RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "PLUS_INT", 
			"PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", "STAR_FLOAT", "DIV_INT", 
			"DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", 
			"GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", 
			"LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", 
			"LEFT_PAREN", "RIGHT_PARENT", "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", 
			"RIGHT_BRACE", "COLON", "DOT", "SEMI", "COMMA"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElSelf'", 
			"'ElseIf'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
			"'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
			"'False'", "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", 
			"'\\.'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
			"'<='", "'>='", "'=\\='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", 
			"'['", "']'", "'{'", "'}'", "':'", "'.'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "REAL_NUMBER", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "COMMENT", 
			"UNTERMINATED_COMMENT", "ERROR_CHAR", "WS", "Integer_literal", "Float_literal", 
			"Boolean_literal", "String_literal", "BODY", "BREAK", "CONTINUE", "DO", 
			"ELSE", "ELSELF", "ELSEIF", "ENDBODY", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
			"IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
			"ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", "STAR_INT", 
			"STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", "OR", "EQUAL", 
			"NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", "GREATER_OR_EQUAL_INT", 
			"NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", "LESS_OR_EQUAL_FLOAT", 
			"GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PARENT", "LEFT_BRACKET", 
			"RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "COLON", "DOT", "SEMI", 
			"COMMA"
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

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 29:
			String_literal_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void String_literal_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:

					String s = this.text;
					this.text = "123123";	
				
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D\u022b\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\3\2\3\2\3\2\3\3\3\3\3\3\7\3\u00b2\n\3\f\3\16\3\u00b5\13\3\3\4\3"+
		"\4\7\4\u00b9\n\4\f\4\16\4\u00bc\13\4\3\4\3\4\3\5\3\5\7\5\u00c2\n\5\f\5"+
		"\16\5\u00c5\13\5\3\5\5\5\u00c8\n\5\3\6\3\6\3\6\3\6\7\6\u00ce\n\6\f\6\16"+
		"\6\u00d1\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00dc\n\7\f\7\16"+
		"\7\u00df\13\7\3\7\3\7\3\b\3\b\3\t\6\t\u00e6\n\t\r\t\16\t\u00e7\3\t\3\t"+
		"\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\5\r\u00f4\n\r\3\16\5\16\u00f7\n\16"+
		"\3\17\3\17\3\17\6\17\u00fc\n\17\r\17\16\17\u00fd\3\20\3\20\7\20\u0102"+
		"\n\20\f\20\16\20\u0105\13\20\3\21\6\21\u0108\n\21\r\21\16\21\u0109\3\21"+
		"\3\21\5\21\u010e\n\21\3\21\5\21\u0111\n\21\3\22\3\22\3\22\3\23\3\23\3"+
		"\23\3\24\3\24\3\24\3\25\3\25\3\25\5\25\u011f\n\25\3\26\3\26\3\27\3\27"+
		"\3\30\3\30\3\30\3\30\5\30\u0129\n\30\3\30\6\30\u012c\n\30\r\30\16\30\u012d"+
		"\3\31\6\31\u0131\n\31\r\31\16\31\u0132\3\32\3\32\3\32\3\32\5\32\u0139"+
		"\n\32\3\32\6\32\u013c\n\32\r\32\16\32\u013d\3\33\3\33\3\34\3\34\3\34\5"+
		"\34\u0145\n\34\3\35\3\35\3\36\3\36\5\36\u014b\n\36\3\37\3\37\7\37\u014f"+
		"\n\37\f\37\16\37\u0152\13\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3"+
		"!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3"+
		"%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3"+
		"(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3"+
		"+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3"+
		".\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61"+
		"\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64"+
		"\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\38\39\39\3:\3"+
		":\3:\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3"+
		"C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\3"+
		"J\3K\3K\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3"+
		"U\3U\4\u00cf\u00dd\2V\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\2\25\2\27"+
		"\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\139"+
		"\f;\r=\16?\17A\20C\21E\22G\23I\24K\25M\26O\27Q\30S\31U\32W\33Y\34[\35"+
		"]\36_\37a c!e\"g#i$k%m&o\'q(s)u*w+y,{-}.\177/\u0081\60\u0083\61\u0085"+
		"\62\u0087\63\u0089\64\u008b\65\u008d\66\u008f\67\u00918\u00939\u0095:"+
		"\u0097;\u0099<\u009b=\u009d>\u009f?\u00a1@\u00a3A\u00a5B\u00a7C\u00a9"+
		"D\3\2\17\4\3\n\f\16\17\4\2\60\60AA\5\2\13\f\16\17\"\"\3\2c|\3\2C\\\3\2"+
		"\62;\4\2--//\4\2GGgg\3\2\60\60\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\5"+
		"\2\62;CHch\3\2\629\2\u0231\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2"+
		"\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\67\3\2\2\2\2"+
		"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3"+
		"\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2"+
		"\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2"+
		"_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3"+
		"\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2"+
		"\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083"+
		"\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2"+
		"\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095"+
		"\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2"+
		"\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7"+
		"\3\2\2\2\2\u00a9\3\2\2\2\3\u00ab\3\2\2\2\5\u00ae\3\2\2\2\7\u00b6\3\2\2"+
		"\2\t\u00bf\3\2\2\2\13\u00c9\3\2\2\2\r\u00d7\3\2\2\2\17\u00e2\3\2\2\2\21"+
		"\u00e5\3\2\2\2\23\u00eb\3\2\2\2\25\u00ed\3\2\2\2\27\u00ef\3\2\2\2\31\u00f3"+
		"\3\2\2\2\33\u00f6\3\2\2\2\35\u00f8\3\2\2\2\37\u00ff\3\2\2\2!\u0107\3\2"+
		"\2\2#\u0112\3\2\2\2%\u0115\3\2\2\2\'\u0118\3\2\2\2)\u011e\3\2\2\2+\u0120"+
		"\3\2\2\2-\u0122\3\2\2\2/\u0128\3\2\2\2\61\u0130\3\2\2\2\63\u0138\3\2\2"+
		"\2\65\u013f\3\2\2\2\67\u0144\3\2\2\29\u0146\3\2\2\2;\u014a\3\2\2\2=\u014c"+
		"\3\2\2\2?\u0156\3\2\2\2A\u015b\3\2\2\2C\u0161\3\2\2\2E\u016a\3\2\2\2G"+
		"\u016d\3\2\2\2I\u0172\3\2\2\2K\u0179\3\2\2\2M\u0180\3\2\2\2O\u0186\3\2"+
		"\2\2Q\u018d\3\2\2\2S\u0196\3\2\2\2U\u019a\3\2\2\2W\u01a3\3\2\2\2Y\u01a6"+
		"\3\2\2\2[\u01b0\3\2\2\2]\u01b7\3\2\2\2_\u01bc\3\2\2\2a\u01c0\3\2\2\2c"+
		"\u01c6\3\2\2\2e\u01cb\3\2\2\2g\u01d1\3\2\2\2i\u01d7\3\2\2\2k\u01d9\3\2"+
		"\2\2m\u01dc\3\2\2\2o\u01de\3\2\2\2q\u01e1\3\2\2\2s\u01e3\3\2\2\2u\u01e6"+
		"\3\2\2\2w\u01e8\3\2\2\2y\u01eb\3\2\2\2{\u01ed\3\2\2\2}\u01ef\3\2\2\2\177"+
		"\u01f2\3\2\2\2\u0081\u01f5\3\2\2\2\u0083\u01f8\3\2\2\2\u0085\u01fb\3\2"+
		"\2\2\u0087\u01fd\3\2\2\2\u0089\u01ff\3\2\2\2\u008b\u0202\3\2\2\2\u008d"+
		"\u0205\3\2\2\2\u008f\u0209\3\2\2\2\u0091\u020c\3\2\2\2\u0093\u020f\3\2"+
		"\2\2\u0095\u0213\3\2\2\2\u0097\u0217\3\2\2\2\u0099\u0219\3\2\2\2\u009b"+
		"\u021b\3\2\2\2\u009d\u021d\3\2\2\2\u009f\u021f\3\2\2\2\u00a1\u0221\3\2"+
		"\2\2\u00a3\u0223\3\2\2\2\u00a5\u0225\3\2\2\2\u00a7\u0227\3\2\2\2\u00a9"+
		"\u0229\3\2\2\2\u00ab\u00ac\5\33\16\2\u00ac\u00ad\5!\21\2\u00ad\4\3\2\2"+
		"\2\u00ae\u00b3\5\23\n\2\u00af\u00b2\5\23\n\2\u00b0\u00b2\5\27\f\2\u00b1"+
		"\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2"+
		"\2\2\u00b3\u00b4\3\2\2\2\u00b4\6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00ba"+
		"\7$\2\2\u00b7\u00b9\5)\25\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba"+
		"\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3\2"+
		"\2\2\u00bd\u00be\5#\22\2\u00be\b\3\2\2\2\u00bf\u00c3\7$\2\2\u00c0\u00c2"+
		"\5)\25\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3"+
		"\u00c4\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c8\t\2"+
		"\2\2\u00c7\u00c6\3\2\2\2\u00c8\n\3\2\2\2\u00c9\u00ca\7,\2\2\u00ca\u00cb"+
		"\7,\2\2\u00cb\u00cf\3\2\2\2\u00cc\u00ce\13\2\2\2\u00cd\u00cc\3\2\2\2\u00ce"+
		"\u00d1\3\2\2\2\u00cf\u00d0\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d2\3\2"+
		"\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00d3\7,\2\2\u00d3\u00d4\7,\2\2\u00d4\u00d5"+
		"\3\2\2\2\u00d5\u00d6\b\6\2\2\u00d6\f\3\2\2\2\u00d7\u00d8\7,\2\2\u00d8"+
		"\u00d9\7,\2\2\u00d9\u00dd\3\2\2\2\u00da\u00dc\13\2\2\2\u00db\u00da\3\2"+
		"\2\2\u00dc\u00df\3\2\2\2\u00dd\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de"+
		"\u00e0\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7\2\2\3\u00e1\16\3\2\2"+
		"\2\u00e2\u00e3\t\3\2\2\u00e3\20\3\2\2\2\u00e4\u00e6\t\4\2\2\u00e5\u00e4"+
		"\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8"+
		"\u00e9\3\2\2\2\u00e9\u00ea\b\t\2\2\u00ea\22\3\2\2\2\u00eb\u00ec\t\5\2"+
		"\2\u00ec\24\3\2\2\2\u00ed\u00ee\t\6\2\2\u00ee\26\3\2\2\2\u00ef\u00f0\t"+
		"\7\2\2\u00f0\30\3\2\2\2\u00f1\u00f4\5\23\n\2\u00f2\u00f4\5\25\13\2\u00f3"+
		"\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\32\3\2\2\2\u00f5\u00f7\t\b\2"+
		"\2\u00f6\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\34\3\2\2\2\u00f8\u00f9"+
		"\t\t\2\2\u00f9\u00fb\5\33\16\2\u00fa\u00fc\5\27\f\2\u00fb\u00fa\3\2\2"+
		"\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\36"+
		"\3\2\2\2\u00ff\u0103\t\n\2\2\u0100\u0102\5\27\f\2\u0101\u0100\3\2\2\2"+
		"\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104 \3"+
		"\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108\5\27\f\2\u0107\u0106\3\2\2\2\u0108"+
		"\u0109\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0110\3\2"+
		"\2\2\u010b\u010d\5\37\20\2\u010c\u010e\5\35\17\2\u010d\u010c\3\2\2\2\u010d"+
		"\u010e\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u0111\5\35\17\2\u0110\u010b\3"+
		"\2\2\2\u0110\u010f\3\2\2\2\u0111\"\3\2\2\2\u0112\u0113\7^\2\2\u0113\u0114"+
		"\n\13\2\2\u0114$\3\2\2\2\u0115\u0116\7^\2\2\u0116\u0117\t\13\2\2\u0117"+
		"&\3\2\2\2\u0118\u0119\7)\2\2\u0119\u011a\7$\2\2\u011a(\3\2\2\2\u011b\u011f"+
		"\n\f\2\2\u011c\u011f\5%\23\2\u011d\u011f\5\'\24\2\u011e\u011b\3\2\2\2"+
		"\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f*\3\2\2\2\u0120\u0121\t"+
		"\r\2\2\u0121,\3\2\2\2\u0122\u0123\t\16\2\2\u0123.\3\2\2\2\u0124\u0125"+
		"\7\62\2\2\u0125\u0129\7z\2\2\u0126\u0127\7\62\2\2\u0127\u0129\7Z\2\2\u0128"+
		"\u0124\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u012c\5+"+
		"\26\2\u012b\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d"+
		"\u012e\3\2\2\2\u012e\60\3\2\2\2\u012f\u0131\5\27\f\2\u0130\u012f\3\2\2"+
		"\2\u0131\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\62"+
		"\3\2\2\2\u0134\u0135\7\62\2\2\u0135\u0139\7q\2\2\u0136\u0137\7\62\2\2"+
		"\u0137\u0139\7Q\2\2\u0138\u0134\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013b"+
		"\3\2\2\2\u013a\u013c\5-\27\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d"+
		"\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\64\3\2\2\2\u013f\u0140\7$\2\2"+
		"\u0140\66\3\2\2\2\u0141\u0145\5\61\31\2\u0142\u0145\5/\30\2\u0143\u0145"+
		"\5\63\32\2\u0144\u0141\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0143\3\2\2\2"+
		"\u01458\3\2\2\2\u0146\u0147\5!\21\2\u0147:\3\2\2\2\u0148\u014b\5c\62\2"+
		"\u0149\u014b\5e\63\2\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b<\3"+
		"\2\2\2\u014c\u0150\7$\2\2\u014d\u014f\5)\25\2\u014e\u014d\3\2\2\2\u014f"+
		"\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2"+
		"\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7$\2\2\u0154\u0155\b\37\3\2\u0155"+
		">\3\2\2\2\u0156\u0157\7D\2\2\u0157\u0158\7q\2\2\u0158\u0159\7f\2\2\u0159"+
		"\u015a\7{\2\2\u015a@\3\2\2\2\u015b\u015c\7D\2\2\u015c\u015d\7t\2\2\u015d"+
		"\u015e\7g\2\2\u015e\u015f\7c\2\2\u015f\u0160\7m\2\2\u0160B\3\2\2\2\u0161"+
		"\u0162\7E\2\2\u0162\u0163\7q\2\2\u0163\u0164\7p\2\2\u0164\u0165\7v\2\2"+
		"\u0165\u0166\7k\2\2\u0166\u0167\7p\2\2\u0167\u0168\7w\2\2\u0168\u0169"+
		"\7g\2\2\u0169D\3\2\2\2\u016a\u016b\7F\2\2\u016b\u016c\7q\2\2\u016cF\3"+
		"\2\2\2\u016d\u016e\7G\2\2\u016e\u016f\7n\2\2\u016f\u0170\7u\2\2\u0170"+
		"\u0171\7g\2\2\u0171H\3\2\2\2\u0172\u0173\7G\2\2\u0173\u0174\7n\2\2\u0174"+
		"\u0175\7U\2\2\u0175\u0176\7g\2\2\u0176\u0177\7n\2\2\u0177\u0178\7h\2\2"+
		"\u0178J\3\2\2\2\u0179\u017a\7G\2\2\u017a\u017b\7n\2\2\u017b\u017c\7u\2"+
		"\2\u017c\u017d\7g\2\2\u017d\u017e\7K\2\2\u017e\u017f\7h\2\2\u017fL\3\2"+
		"\2\2\u0180\u0181\7G\2\2\u0181\u0182\7p\2\2\u0182\u0183\7f\2\2\u0183\u0184"+
		"\7K\2\2\u0184\u0185\7h\2\2\u0185N\3\2\2\2\u0186\u0187\7G\2\2\u0187\u0188"+
		"\7p\2\2\u0188\u0189\7f\2\2\u0189\u018a\7H\2\2\u018a\u018b\7q\2\2\u018b"+
		"\u018c\7t\2\2\u018cP\3\2\2\2\u018d\u018e\7G\2\2\u018e\u018f\7p\2\2\u018f"+
		"\u0190\7f\2\2\u0190\u0191\7Y\2\2\u0191\u0192\7j\2\2\u0192\u0193\7k\2\2"+
		"\u0193\u0194\7n\2\2\u0194\u0195\7g\2\2\u0195R\3\2\2\2\u0196\u0197\7H\2"+
		"\2\u0197\u0198\7q\2\2\u0198\u0199\7t\2\2\u0199T\3\2\2\2\u019a\u019b\7"+
		"H\2\2\u019b\u019c\7w\2\2\u019c\u019d\7p\2\2\u019d\u019e\7e\2\2\u019e\u019f"+
		"\7v\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2\7p\2\2\u01a2"+
		"V\3\2\2\2\u01a3\u01a4\7K\2\2\u01a4\u01a5\7h\2\2\u01a5X\3\2\2\2\u01a6\u01a7"+
		"\7R\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa\7c\2\2\u01aa"+
		"\u01ab\7o\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad\7v\2\2\u01ad\u01ae\7g\2\2"+
		"\u01ae\u01af\7t\2\2\u01afZ\3\2\2\2\u01b0\u01b1\7T\2\2\u01b1\u01b2\7g\2"+
		"\2\u01b2\u01b3\7v\2\2\u01b3\u01b4\7w\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6"+
		"\7p\2\2\u01b6\\\3\2\2\2\u01b7\u01b8\7V\2\2\u01b8\u01b9\7j\2\2\u01b9\u01ba"+
		"\7g\2\2\u01ba\u01bb\7p\2\2\u01bb^\3\2\2\2\u01bc\u01bd\7X\2\2\u01bd\u01be"+
		"\7c\2\2\u01be\u01bf\7t\2\2\u01bf`\3\2\2\2\u01c0\u01c1\7Y\2\2\u01c1\u01c2"+
		"\7j\2\2\u01c2\u01c3\7k\2\2\u01c3\u01c4\7n\2\2\u01c4\u01c5\7g\2\2\u01c5"+
		"b\3\2\2\2\u01c6\u01c7\7V\2\2\u01c7\u01c8\7t\2\2\u01c8\u01c9\7w\2\2\u01c9"+
		"\u01ca\7g\2\2\u01cad\3\2\2\2\u01cb\u01cc\7H\2\2\u01cc\u01cd\7c\2\2\u01cd"+
		"\u01ce\7n\2\2\u01ce\u01cf\7u\2\2\u01cf\u01d0\7g\2\2\u01d0f\3\2\2\2\u01d1"+
		"\u01d2\7G\2\2\u01d2\u01d3\7p\2\2\u01d3\u01d4\7f\2\2\u01d4\u01d5\7F\2\2"+
		"\u01d5\u01d6\7q\2\2\u01d6h\3\2\2\2\u01d7\u01d8\7-\2\2\u01d8j\3\2\2\2\u01d9"+
		"\u01da\7-\2\2\u01da\u01db\7\60\2\2\u01dbl\3\2\2\2\u01dc\u01dd\7/\2\2\u01dd"+
		"n\3\2\2\2\u01de\u01df\7/\2\2\u01df\u01e0\7\60\2\2\u01e0p\3\2\2\2\u01e1"+
		"\u01e2\7,\2\2\u01e2r\3\2\2\2\u01e3\u01e4\7,\2\2\u01e4\u01e5\7\60\2\2\u01e5"+
		"t\3\2\2\2\u01e6\u01e7\7^\2\2\u01e7v\3\2\2\2\u01e8\u01e9\7^\2\2\u01e9\u01ea"+
		"\7\60\2\2\u01eax\3\2\2\2\u01eb\u01ec\7\'\2\2\u01ecz\3\2\2\2\u01ed\u01ee"+
		"\7#\2\2\u01ee|\3\2\2\2\u01ef\u01f0\7(\2\2\u01f0\u01f1\7(\2\2\u01f1~\3"+
		"\2\2\2\u01f2\u01f3\7~\2\2\u01f3\u01f4\7~\2\2\u01f4\u0080\3\2\2\2\u01f5"+
		"\u01f6\7?\2\2\u01f6\u01f7\7?\2\2\u01f7\u0082\3\2\2\2\u01f8\u01f9\7#\2"+
		"\2\u01f9\u01fa\7?\2\2\u01fa\u0084\3\2\2\2\u01fb\u01fc\7>\2\2\u01fc\u0086"+
		"\3\2\2\2\u01fd\u01fe\7@\2\2\u01fe\u0088\3\2\2\2\u01ff\u0200\7>\2\2\u0200"+
		"\u0201\7?\2\2\u0201\u008a\3\2\2\2\u0202\u0203\7@\2\2\u0203\u0204\7?\2"+
		"\2\u0204\u008c\3\2\2\2\u0205\u0206\7?\2\2\u0206\u0207\7^\2\2\u0207\u0208"+
		"\7?\2\2\u0208\u008e\3\2\2\2\u0209\u020a\7>\2\2\u020a\u020b\7\60\2\2\u020b"+
		"\u0090\3\2\2\2\u020c\u020d\7@\2\2\u020d\u020e\7\60\2\2\u020e\u0092\3\2"+
		"\2\2\u020f\u0210\7>\2\2\u0210\u0211\7?\2\2\u0211\u0212\7\60\2\2\u0212"+
		"\u0094\3\2\2\2\u0213\u0214\7@\2\2\u0214\u0215\7?\2\2\u0215\u0216\7\60"+
		"\2\2\u0216\u0096\3\2\2\2\u0217\u0218\7*\2\2\u0218\u0098\3\2\2\2\u0219"+
		"\u021a\7+\2\2\u021a\u009a\3\2\2\2\u021b\u021c\7]\2\2\u021c\u009c\3\2\2"+
		"\2\u021d\u021e\7_\2\2\u021e\u009e\3\2\2\2\u021f\u0220\7}\2\2\u0220\u00a0"+
		"\3\2\2\2\u0221\u0222\7\177\2\2\u0222\u00a2\3\2\2\2\u0223\u0224\7<\2\2"+
		"\u0224\u00a4\3\2\2\2\u0225\u0226\7\60\2\2\u0226\u00a6\3\2\2\2\u0227\u0228"+
		"\7=\2\2\u0228\u00a8\3\2\2\2\u0229\u022a\7.\2\2\u022a\u00aa\3\2\2\2\33"+
		"\2\u00b1\u00b3\u00ba\u00c3\u00c7\u00cf\u00dd\u00e7\u00f3\u00f6\u00fd\u0103"+
		"\u0109\u010d\u0110\u011e\u0128\u012d\u0132\u0138\u013d\u0144\u014a\u0150"+
		"\4\b\2\2\3\37\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}