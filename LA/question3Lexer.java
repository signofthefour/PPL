// Generated from question3.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class question3Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		REAL=1, STRING=2, QUOTE=3, WS=4;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "DOT", "EXPO", "SIGN", "SCIEN", "SING_QUO", "DOU_QUO", "REAL", 
			"STRING", "QUOTE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "REAL", "STRING", "QUOTE", "WS"
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


	public question3Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "question3.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6Q\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\5\5\"\n\5\3\6\3\6\3\6\6\6"+
		"\'\n\6\r\6\16\6(\3\7\3\7\3\b\3\b\3\b\3\t\3\t\6\t\62\n\t\r\t\16\t\63\3"+
		"\t\3\t\6\t8\n\t\r\t\16\t9\3\t\5\t=\n\t\3\t\5\t@\n\t\3\n\3\n\3\n\6\nE\n"+
		"\n\r\n\16\nF\3\13\3\13\3\f\6\fL\n\f\r\f\16\fM\3\f\3\f\2\2\r\3\2\5\2\7"+
		"\2\t\2\13\2\r\2\17\2\21\3\23\4\25\5\27\6\3\2\7\3\2\62;\5\2--//~~\3\2)"+
		")\3\2\f\f\5\2\13\f\17\17\"\"\2R\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t!\3\2\2\2\13#\3"+
		"\2\2\2\r*\3\2\2\2\17,\3\2\2\2\21/\3\2\2\2\23D\3\2\2\2\25H\3\2\2\2\27K"+
		"\3\2\2\2\31\32\t\2\2\2\32\4\3\2\2\2\33\34\7\60\2\2\34\6\3\2\2\2\35\36"+
		"\7g\2\2\36\37\5\t\5\2\37\b\3\2\2\2 \"\t\3\2\2! \3\2\2\2!\"\3\2\2\2\"\n"+
		"\3\2\2\2#$\5\7\4\2$&\5\t\5\2%\'\5\3\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2"+
		"()\3\2\2\2)\f\3\2\2\2*+\t\4\2\2+\16\3\2\2\2,-\5\r\7\2-.\5\r\7\2.\20\3"+
		"\2\2\2/\61\5\t\5\2\60\62\5\3\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2"+
		"\2\2\63\64\3\2\2\2\64?\3\2\2\2\65\67\5\5\3\2\668\5\3\2\2\67\66\3\2\2\2"+
		"89\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;=\5\13\6\2<;\3\2\2\2<=\3\2"+
		"\2\2=@\3\2\2\2>@\5\13\6\2?\65\3\2\2\2?>\3\2\2\2@\22\3\2\2\2AB\n\4\2\2"+
		"BE\n\5\2\2CE\5\17\b\2DA\3\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2"+
		"\2G\24\3\2\2\2HI\t\4\2\2I\26\3\2\2\2JL\t\6\2\2KJ\3\2\2\2LM\3\2\2\2MK\3"+
		"\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\f\2\2P\30\3\2\2\2\f\2!(\639<?DFM\3\b\2"+
		"\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}