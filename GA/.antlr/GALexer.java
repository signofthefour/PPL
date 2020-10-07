// Generated from /home/khanh/Documents/schoolLife/201/PPL/GA/GA.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GALexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INT=1, FLOAT=2, RETURN=3, ID=4, INTLIT=5, FLOATLIT=6, LB=7, RB=8, SM=9, 
		CM=10, EQ=11, LP=12, RP=13, ADDOP=14, SUBOP=15, MULOP=16, DIVOP=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"INT", "FLOAT", "RETURN", "NUMBER", "DOT", "EXPO", "SIGN", "SCIEN", "ID", 
			"INTLIT", "FLOATLIT", "LB", "RB", "SM", "CM", "EQ", "LP", "RP", "ADDOP", 
			"SUBOP", "MULOP", "DIVOP", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'int'", "'float'", "'return'", null, null, null, "'{'", "'}'", 
			"';'", "','", "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INT", "FLOAT", "RETURN", "ID", "INTLIT", "FLOATLIT", "LB", "RB", 
			"SM", "CM", "EQ", "LP", "RP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "WS"
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


	public GALexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "GA.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\u008e\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2"+
		"\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3"+
		"\5\3\6\3\6\3\7\3\7\3\7\3\b\5\bK\n\b\3\t\3\t\6\tO\n\t\r\t\16\tP\3\n\3\n"+
		"\7\nU\n\n\f\n\16\nX\13\n\3\13\3\13\6\13\\\n\13\r\13\16\13]\3\f\3\f\6\f"+
		"b\n\f\r\f\16\fc\3\f\3\f\6\fh\n\f\r\f\16\fi\3\f\5\fm\n\f\3\f\5\fp\n\f\3"+
		"\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24"+
		"\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\6\30\u0089\n\30\r\30\16\30\u008a"+
		"\3\30\3\30\2\2\31\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21\2\23\6\25\7\27\b\31"+
		"\t\33\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\3\2\6\3\2\62;\3\2c"+
		"|\4\2\62;c|\5\2\13\f\16\17\"\"\2\u0091\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2"+
		"\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2"+
		"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2"+
		"\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2\2\5\65\3\2\2"+
		"\2\7;\3\2\2\2\tB\3\2\2\2\13D\3\2\2\2\rF\3\2\2\2\17J\3\2\2\2\21L\3\2\2"+
		"\2\23R\3\2\2\2\25Y\3\2\2\2\27_\3\2\2\2\31q\3\2\2\2\33s\3\2\2\2\35u\3\2"+
		"\2\2\37w\3\2\2\2!y\3\2\2\2#{\3\2\2\2%}\3\2\2\2\'\177\3\2\2\2)\u0081\3"+
		"\2\2\2+\u0083\3\2\2\2-\u0085\3\2\2\2/\u0088\3\2\2\2\61\62\7k\2\2\62\63"+
		"\7p\2\2\63\64\7v\2\2\64\4\3\2\2\2\65\66\7h\2\2\66\67\7n\2\2\678\7q\2\2"+
		"89\7c\2\29:\7v\2\2:\6\3\2\2\2;<\7t\2\2<=\7g\2\2=>\7v\2\2>?\7w\2\2?@\7"+
		"t\2\2@A\7p\2\2A\b\3\2\2\2BC\t\2\2\2C\n\3\2\2\2DE\7\60\2\2E\f\3\2\2\2F"+
		"G\7g\2\2GH\5\17\b\2H\16\3\2\2\2IK\7/\2\2JI\3\2\2\2JK\3\2\2\2K\20\3\2\2"+
		"\2LN\5\r\7\2MO\5\t\5\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q\22\3\2"+
		"\2\2RV\t\3\2\2SU\t\4\2\2TS\3\2\2\2UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\24\3"+
		"\2\2\2XV\3\2\2\2Y[\5\17\b\2Z\\\t\2\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2"+
		"]^\3\2\2\2^\26\3\2\2\2_a\5\17\b\2`b\5\t\5\2a`\3\2\2\2bc\3\2\2\2ca\3\2"+
		"\2\2cd\3\2\2\2do\3\2\2\2eg\5\13\6\2fh\5\t\5\2gf\3\2\2\2hi\3\2\2\2ig\3"+
		"\2\2\2ij\3\2\2\2jl\3\2\2\2km\5\21\t\2lk\3\2\2\2lm\3\2\2\2mp\3\2\2\2np"+
		"\5\21\t\2oe\3\2\2\2on\3\2\2\2p\30\3\2\2\2qr\7}\2\2r\32\3\2\2\2st\7\177"+
		"\2\2t\34\3\2\2\2uv\7=\2\2v\36\3\2\2\2wx\7.\2\2x \3\2\2\2yz\7?\2\2z\"\3"+
		"\2\2\2{|\7*\2\2|$\3\2\2\2}~\7+\2\2~&\3\2\2\2\177\u0080\7-\2\2\u0080(\3"+
		"\2\2\2\u0081\u0082\7/\2\2\u0082*\3\2\2\2\u0083\u0084\7,\2\2\u0084,\3\2"+
		"\2\2\u0085\u0086\7\61\2\2\u0086.\3\2\2\2\u0087\u0089\t\5\2\2\u0088\u0087"+
		"\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b"+
		"\u008c\3\2\2\2\u008c\u008d\b\30\2\2\u008d\60\3\2\2\2\f\2JPV]cilo\u008a"+
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