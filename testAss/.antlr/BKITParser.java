// Generated from /home/khanh/Documents/schoolLife/201/PPL/testAss/BKIT.g4 by ANTLR 4.8
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
		VAR=1, FUNCTION=2, BODY=3, ELSE=4, ENDFOR=5, IF=6, ENDDO=7, BREAK=8, ELSEIF=9, 
		ENDWHILE=10, PARAMETER=11, WHILE=12, CONTINUE=13, ENDBODY=14, FOR=15, 
		RETURN=16, TRUE=17, DO=18, ENDIF=19, THEN=20, FALSE=21, WS=22, IDENTIFIER=23, 
		LB=24, RB=25, LK=26, RK=27, LP=28, RP=29, SEMI=30, COLON=31, CM=32, DOT=33, 
		INTERGER=34, FLOAT=35, BOLEAN=36, ADDOP=37, SUBOP=38, MULOP=39, DIVOP=40, 
		AS=41, ERROR_CHAR=42, UNCLOSE_STRING=43, ILLEGAL_ESCAPE=44, UNTERMINATED_COMMENT=45, 
		NUM=46;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_var_list = 2, RULE_non_initted_var = 3, 
		RULE_initted_var = 4, RULE_literals = 5, RULE_array_list = 6, RULE_int_array = 7, 
		RULE_float_array = 8;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "non_initted_var", "initted_var", 
			"literals", "array_list", "int_array", "float_array"
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
			"LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "INTERGER", 
			"FLOAT", "BOLEAN", "ADDOP", "SUBOP", "MULOP", "DIVOP", "AS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "NUM"
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
		public Var_declareContext var_declare() {
			return getRuleContext(Var_declareContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			var_declare();
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

	public static class Var_declareContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(BKITParser.VAR, 0); }
		public TerminalNode COLON() { return getToken(BKITParser.COLON, 0); }
		public Var_listContext var_list() {
			return getRuleContext(Var_listContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public Var_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare; }
	}

	public final Var_declareContext var_declare() throws RecognitionException {
		Var_declareContext _localctx = new Var_declareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(20);
			match(VAR);
			setState(21);
			match(COLON);
			setState(22);
			var_list();
			setState(24);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(23);
				match(AS);
				}
			}

			setState(26);
			match(SEMI);
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

	public static class Var_listContext extends ParserRuleContext {
		public List<Initted_varContext> initted_var() {
			return getRuleContexts(Initted_varContext.class);
		}
		public Initted_varContext initted_var(int i) {
			return getRuleContext(Initted_varContext.class,i);
		}
		public List<Non_initted_varContext> non_initted_var() {
			return getRuleContexts(Non_initted_varContext.class);
		}
		public Non_initted_varContext non_initted_var(int i) {
			return getRuleContext(Non_initted_varContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Var_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_list; }
	}

	public final Var_listContext var_list() throws RecognitionException {
		Var_listContext _localctx = new Var_listContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_var_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(30);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(28);
				initted_var();
				}
				break;
			case 2:
				{
				setState(29);
				non_initted_var();
				}
				break;
			}
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(32);
				match(CM);
				setState(35);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(33);
					initted_var();
					}
					break;
				case 2:
					{
					setState(34);
					non_initted_var();
					}
					break;
				}
				}
				}
				setState(41);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Non_initted_varContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public List<TerminalNode> LK() { return getTokens(BKITParser.LK); }
		public TerminalNode LK(int i) {
			return getToken(BKITParser.LK, i);
		}
		public List<TerminalNode> NUM() { return getTokens(BKITParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(BKITParser.NUM, i);
		}
		public List<TerminalNode> RK() { return getTokens(BKITParser.RK); }
		public TerminalNode RK(int i) {
			return getToken(BKITParser.RK, i);
		}
		public Non_initted_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_non_initted_var; }
	}

	public final Non_initted_varContext non_initted_var() throws RecognitionException {
		Non_initted_varContext _localctx = new Non_initted_varContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_non_initted_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			match(IDENTIFIER);
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LK) {
				{
				{
				setState(43);
				match(LK);
				setState(44);
				match(NUM);
				setState(45);
				match(RK);
				}
				}
				setState(50);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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

	public static class Initted_varContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public List<TerminalNode> LK() { return getTokens(BKITParser.LK); }
		public TerminalNode LK(int i) {
			return getToken(BKITParser.LK, i);
		}
		public List<TerminalNode> NUM() { return getTokens(BKITParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(BKITParser.NUM, i);
		}
		public List<TerminalNode> RK() { return getTokens(BKITParser.RK); }
		public TerminalNode RK(int i) {
			return getToken(BKITParser.RK, i);
		}
		public Initted_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initted_var; }
	}

	public final Initted_varContext initted_var() throws RecognitionException {
		Initted_varContext _localctx = new Initted_varContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_initted_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(IDENTIFIER);
			setState(57);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LK) {
				{
				{
				setState(52);
				match(LK);
				setState(53);
				match(NUM);
				setState(54);
				match(RK);
				}
				}
				setState(59);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(60);
			match(AS);
			setState(61);
			literals();
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

	public static class LiteralsContext extends ParserRuleContext {
		public TerminalNode INTERGER() { return getToken(BKITParser.INTERGER, 0); }
		public TerminalNode FLOAT() { return getToken(BKITParser.FLOAT, 0); }
		public TerminalNode BOLEAN() { return getToken(BKITParser.BOLEAN, 0); }
		public Array_listContext array_list() {
			return getRuleContext(Array_listContext.class,0);
		}
		public LiteralsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literals; }
	}

	public final LiteralsContext literals() throws RecognitionException {
		LiteralsContext _localctx = new LiteralsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_literals);
		try {
			setState(67);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTERGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(63);
				match(INTERGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(64);
				match(FLOAT);
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(65);
				match(BOLEAN);
				}
				break;
			case LB:
				enterOuterAlt(_localctx, 4);
				{
				setState(66);
				array_list();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Array_listContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKITParser.LB, 0); }
		public List<Array_listContext> array_list() {
			return getRuleContexts(Array_listContext.class);
		}
		public Array_listContext array_list(int i) {
			return getRuleContext(Array_listContext.class,i);
		}
		public Int_arrayContext int_array() {
			return getRuleContext(Int_arrayContext.class,0);
		}
		public Float_arrayContext float_array() {
			return getRuleContext(Float_arrayContext.class,0);
		}
		public TerminalNode RB() { return getToken(BKITParser.RB, 0); }
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Array_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_list; }
	}

	public final Array_listContext array_list() throws RecognitionException {
		Array_listContext _localctx = new Array_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_array_list);
		int _la;
		try {
			setState(82);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(69);
				match(LB);
				setState(70);
				array_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(71);
				int_array();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(72);
				float_array();
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(73);
					match(CM);
					setState(74);
					array_list();
					}
					}
					setState(79);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(80);
				match(RB);
				}
				break;
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

	public static class Int_arrayContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKITParser.LB, 0); }
		public List<TerminalNode> INTERGER() { return getTokens(BKITParser.INTERGER); }
		public TerminalNode INTERGER(int i) {
			return getToken(BKITParser.INTERGER, i);
		}
		public TerminalNode RB() { return getToken(BKITParser.RB, 0); }
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Int_arrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_int_array; }
	}

	public final Int_arrayContext int_array() throws RecognitionException {
		Int_arrayContext _localctx = new Int_arrayContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_int_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(LB);
			setState(85);
			match(INTERGER);
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(86);
				match(CM);
				setState(87);
				match(INTERGER);
				}
				}
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(93);
			match(RB);
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

	public static class Float_arrayContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKITParser.LB, 0); }
		public List<TerminalNode> FLOAT() { return getTokens(BKITParser.FLOAT); }
		public TerminalNode FLOAT(int i) {
			return getToken(BKITParser.FLOAT, i);
		}
		public TerminalNode RB() { return getToken(BKITParser.RB, 0); }
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Float_arrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_array; }
	}

	public final Float_arrayContext float_array() throws RecognitionException {
		Float_arrayContext _localctx = new Float_arrayContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_float_array);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(LB);
			setState(96);
			match(FLOAT);
			setState(101);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(97);
				match(CM);
				setState(98);
				match(FLOAT);
				}
				}
				setState(103);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(104);
			match(RB);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60m\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\5\3\33\n\3\3\3\3\3\3\4\3\4\5\4!\n\4\3\4\3\4\3\4\5\4&\n\4"+
		"\7\4(\n\4\f\4\16\4+\13\4\3\5\3\5\3\5\3\5\7\5\61\n\5\f\5\16\5\64\13\5\3"+
		"\6\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7"+
		"F\n\7\3\b\3\b\3\b\3\b\3\b\3\b\7\bN\n\b\f\b\16\bQ\13\b\3\b\3\b\5\bU\n\b"+
		"\3\t\3\t\3\t\3\t\7\t[\n\t\f\t\16\t^\13\t\3\t\3\t\3\n\3\n\3\n\3\n\7\nf"+
		"\n\n\f\n\16\ni\13\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2q\2\24"+
		"\3\2\2\2\4\26\3\2\2\2\6 \3\2\2\2\b,\3\2\2\2\n\65\3\2\2\2\fE\3\2\2\2\16"+
		"T\3\2\2\2\20V\3\2\2\2\22a\3\2\2\2\24\25\5\4\3\2\25\3\3\2\2\2\26\27\7\3"+
		"\2\2\27\30\7!\2\2\30\32\5\6\4\2\31\33\7+\2\2\32\31\3\2\2\2\32\33\3\2\2"+
		"\2\33\34\3\2\2\2\34\35\7 \2\2\35\5\3\2\2\2\36!\5\n\6\2\37!\5\b\5\2 \36"+
		"\3\2\2\2 \37\3\2\2\2!)\3\2\2\2\"%\7\"\2\2#&\5\n\6\2$&\5\b\5\2%#\3\2\2"+
		"\2%$\3\2\2\2&(\3\2\2\2\'\"\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\7\3"+
		"\2\2\2+)\3\2\2\2,\62\7\31\2\2-.\7\34\2\2./\7\60\2\2/\61\7\35\2\2\60-\3"+
		"\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\t\3\2\2\2\64\62\3"+
		"\2\2\2\65;\7\31\2\2\66\67\7\34\2\2\678\7\60\2\28:\7\35\2\29\66\3\2\2\2"+
		":=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7+\2\2?@\5\f\7\2"+
		"@\13\3\2\2\2AF\7$\2\2BF\7%\2\2CF\7&\2\2DF\5\16\b\2EA\3\2\2\2EB\3\2\2\2"+
		"EC\3\2\2\2ED\3\2\2\2F\r\3\2\2\2GH\7\32\2\2HU\5\16\b\2IU\5\20\t\2JO\5\22"+
		"\n\2KL\7\"\2\2LN\5\16\b\2MK\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2PR\3"+
		"\2\2\2QO\3\2\2\2RS\7\33\2\2SU\3\2\2\2TG\3\2\2\2TI\3\2\2\2TJ\3\2\2\2U\17"+
		"\3\2\2\2VW\7\32\2\2W\\\7$\2\2XY\7\"\2\2Y[\7$\2\2ZX\3\2\2\2[^\3\2\2\2\\"+
		"Z\3\2\2\2\\]\3\2\2\2]_\3\2\2\2^\\\3\2\2\2_`\7\33\2\2`\21\3\2\2\2ab\7\32"+
		"\2\2bg\7%\2\2cd\7\"\2\2df\7%\2\2ec\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2"+
		"\2hj\3\2\2\2ig\3\2\2\2jk\7\33\2\2k\23\3\2\2\2\r\32 %)\62;EOT\\g";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}