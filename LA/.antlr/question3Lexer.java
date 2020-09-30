// Generated from /home/khanh/Documents/schoolLife/201/PPL/LA/question3.g4 by ANTLR 4.8
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
		REAL=1, STRING=2, WS=3;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUMBER", "DOT", "EXPO", "SIGN", "SCIEN", "SING_QUO", "DOU_QUO", "REAL", 
			"STRING", "WS"
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
			null, "REAL", "STRING", "WS"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5O\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\5\5 \n\5\3\6\3\6\3\6\6\6%\n\6\r\6"+
		"\16\6&\3\7\3\7\3\b\3\b\3\b\3\t\3\t\6\t\60\n\t\r\t\16\t\61\3\t\3\t\6\t"+
		"\66\n\t\r\t\16\t\67\3\t\5\t;\n\t\3\t\5\t>\n\t\3\n\3\n\3\n\6\nC\n\n\r\n"+
		"\16\nD\3\n\3\n\3\13\6\13J\n\13\r\13\16\13K\3\13\3\13\2\2\f\3\2\5\2\7\2"+
		"\t\2\13\2\r\2\17\2\21\3\23\4\25\5\3\2\6\3\2\62;\5\2--//~~\3\2))\5\2\13"+
		"\f\17\17\"\"\2P\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5"+
		"\31\3\2\2\2\7\33\3\2\2\2\t\37\3\2\2\2\13!\3\2\2\2\r(\3\2\2\2\17*\3\2\2"+
		"\2\21-\3\2\2\2\23?\3\2\2\2\25I\3\2\2\2\27\30\t\2\2\2\30\4\3\2\2\2\31\32"+
		"\7\60\2\2\32\6\3\2\2\2\33\34\7g\2\2\34\35\5\t\5\2\35\b\3\2\2\2\36 \t\3"+
		"\2\2\37\36\3\2\2\2\37 \3\2\2\2 \n\3\2\2\2!\"\5\7\4\2\"$\5\t\5\2#%\5\3"+
		"\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\f\3\2\2\2()\t\4\2\2)\16"+
		"\3\2\2\2*+\5\r\7\2+,\5\r\7\2,\20\3\2\2\2-/\5\t\5\2.\60\5\3\2\2/.\3\2\2"+
		"\2\60\61\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62=\3\2\2\2\63\65\5\5\3\2\64"+
		"\66\5\3\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3"+
		"\2\2\29;\5\13\6\2:9\3\2\2\2:;\3\2\2\2;>\3\2\2\2<>\5\13\6\2=\63\3\2\2\2"+
		"=<\3\2\2\2>\22\3\2\2\2?B\5\r\7\2@C\n\4\2\2AC\5\17\b\2B@\3\2\2\2BA\3\2"+
		"\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2FG\5\r\7\2G\24\3\2\2\2HJ\t"+
		"\5\2\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\13\2\2N\26"+
		"\3\2\2\2\f\2\37&\61\67:=BDK\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}