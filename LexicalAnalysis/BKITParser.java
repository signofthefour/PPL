// Generated from BKIT.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITParser extends Parser {
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
	public static final int
		RULE_program = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"program"
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

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D\7\4\2\t\2\3\2\3"+
		"\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5\3\2\2\2\5\3\3\2\2\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}