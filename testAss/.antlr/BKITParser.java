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
		INTEGER=34, FLOAT=35, BOLEAN=36, ADDOP=37, SUBOP=38, MULOP=39, DIVOP=40, 
		AS=41, ERROR_CHAR=42, UNCLOSE_STRING=43, ILLEGAL_ESCAPE=44, UNTERMINATED_COMMENT=45;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_var_list = 2, RULE_non_initted_var = 3, 
		RULE_initted_var = 4, RULE_scalar_init = 5, RULE_composite_init = 6, RULE_scalar_var = 7, 
		RULE_composite_var = 8, RULE_literals = 9, RULE_int_array = 10, RULE_float_array = 11, 
		RULE_array_list = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "non_initted_var", "initted_var", 
			"scalar_init", "composite_init", "scalar_var", "composite_var", "literals", 
			"int_array", "float_array", "array_list"
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
			setState(26);
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
			setState(28);
			match(VAR);
			setState(29);
			match(COLON);
			setState(30);
			var_list();
			setState(32);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(31);
				match(AS);
				}
			}

			setState(34);
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
			setState(38);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(36);
				initted_var();
				}
				break;
			case 2:
				{
				setState(37);
				non_initted_var();
				}
				break;
			}
			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(40);
				match(CM);
				setState(43);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(41);
					initted_var();
					}
					break;
				case 2:
					{
					setState(42);
					non_initted_var();
					}
					break;
				}
				}
				}
				setState(49);
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
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public Composite_varContext composite_var() {
			return getRuleContext(Composite_varContext.class,0);
		}
		public Non_initted_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_non_initted_var; }
	}

	public final Non_initted_varContext non_initted_var() throws RecognitionException {
		Non_initted_varContext _localctx = new Non_initted_varContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_non_initted_var);
		try {
			setState(52);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				scalar_var();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				composite_var();
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

	public static class Initted_varContext extends ParserRuleContext {
		public Scalar_initContext scalar_init() {
			return getRuleContext(Scalar_initContext.class,0);
		}
		public Composite_initContext composite_init() {
			return getRuleContext(Composite_initContext.class,0);
		}
		public Initted_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initted_var; }
	}

	public final Initted_varContext initted_var() throws RecognitionException {
		Initted_varContext _localctx = new Initted_varContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_initted_var);
		try {
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				scalar_init();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				composite_init();
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

	public static class Scalar_initContext extends ParserRuleContext {
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public Scalar_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalar_init; }
	}

	public final Scalar_initContext scalar_init() throws RecognitionException {
		Scalar_initContext _localctx = new Scalar_initContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_scalar_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			scalar_var();
			setState(59);
			match(AS);
			setState(60);
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

	public static class Composite_initContext extends ParserRuleContext {
		public Composite_varContext composite_var() {
			return getRuleContext(Composite_varContext.class,0);
		}
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public Composite_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_init; }
	}

	public final Composite_initContext composite_init() throws RecognitionException {
		Composite_initContext _localctx = new Composite_initContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_composite_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			composite_var();
			setState(63);
			match(AS);
			setState(64);
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

	public static class Scalar_varContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public Scalar_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalar_var; }
	}

	public final Scalar_varContext scalar_var() throws RecognitionException {
		Scalar_varContext _localctx = new Scalar_varContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_scalar_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(IDENTIFIER);
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

	public static class Composite_varContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public List<TerminalNode> LK() { return getTokens(BKITParser.LK); }
		public TerminalNode LK(int i) {
			return getToken(BKITParser.LK, i);
		}
		public List<TerminalNode> INTEGER() { return getTokens(BKITParser.INTEGER); }
		public TerminalNode INTEGER(int i) {
			return getToken(BKITParser.INTEGER, i);
		}
		public List<TerminalNode> RK() { return getTokens(BKITParser.RK); }
		public TerminalNode RK(int i) {
			return getToken(BKITParser.RK, i);
		}
		public Composite_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_var; }
	}

	public final Composite_varContext composite_var() throws RecognitionException {
		Composite_varContext _localctx = new Composite_varContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_composite_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(IDENTIFIER);
			setState(72); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(69);
				match(LK);
				setState(70);
				match(INTEGER);
				setState(71);
				match(RK);
				}
				}
				setState(74); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LK );
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
		public TerminalNode INTEGER() { return getToken(BKITParser.INTEGER, 0); }
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
		enterRule(_localctx, 18, RULE_literals);
		try {
			setState(80);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				match(INTEGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(77);
				match(FLOAT);
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(78);
				match(BOLEAN);
				}
				break;
			case LB:
				enterOuterAlt(_localctx, 4);
				{
				setState(79);
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

	public static class Int_arrayContext extends ParserRuleContext {
		public List<TerminalNode> INTEGER() { return getTokens(BKITParser.INTEGER); }
		public TerminalNode INTEGER(int i) {
			return getToken(BKITParser.INTEGER, i);
		}
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
		enterRule(_localctx, 20, RULE_int_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(INTEGER);
			setState(87);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(83);
					match(CM);
					setState(84);
					match(INTEGER);
					}
					} 
				}
				setState(89);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
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

	public static class Float_arrayContext extends ParserRuleContext {
		public List<TerminalNode> FLOAT() { return getTokens(BKITParser.FLOAT); }
		public TerminalNode FLOAT(int i) {
			return getToken(BKITParser.FLOAT, i);
		}
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
		enterRule(_localctx, 22, RULE_float_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(FLOAT);
			setState(95);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(91);
					match(CM);
					setState(92);
					match(FLOAT);
					}
					} 
				}
				setState(97);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
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

	public static class Array_listContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(BKITParser.LB, 0); }
		public TerminalNode RB() { return getToken(BKITParser.RB, 0); }
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
		enterRule(_localctx, 24, RULE_array_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			match(LB);
			setState(102);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				{
				setState(99);
				array_list();
				}
				break;
			case INTEGER:
				{
				setState(100);
				int_array();
				}
				break;
			case FLOAT:
				{
				setState(101);
				float_array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(104);
				match(CM);
				setState(105);
				array_list();
				}
				}
				setState(110);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(111);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/t\4\2\t\2\4\3\t\3"+
		"\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f"+
		"\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3\3\3\4\3"+
		"\4\5\4)\n\4\3\4\3\4\3\4\5\4.\n\4\7\4\60\n\4\f\4\16\4\63\13\4\3\5\3\5\5"+
		"\5\67\n\5\3\6\3\6\5\6;\n\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\n"+
		"\3\n\3\n\3\n\6\nK\n\n\r\n\16\nL\3\13\3\13\3\13\3\13\5\13S\n\13\3\f\3\f"+
		"\3\f\7\fX\n\f\f\f\16\f[\13\f\3\r\3\r\3\r\7\r`\n\r\f\r\16\rc\13\r\3\16"+
		"\3\16\3\16\3\16\5\16i\n\16\3\16\3\16\7\16m\n\16\f\16\16\16p\13\16\3\16"+
		"\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2u\2\34\3\2\2\2"+
		"\4\36\3\2\2\2\6(\3\2\2\2\b\66\3\2\2\2\n:\3\2\2\2\f<\3\2\2\2\16@\3\2\2"+
		"\2\20D\3\2\2\2\22F\3\2\2\2\24R\3\2\2\2\26T\3\2\2\2\30\\\3\2\2\2\32d\3"+
		"\2\2\2\34\35\5\4\3\2\35\3\3\2\2\2\36\37\7\3\2\2\37 \7!\2\2 \"\5\6\4\2"+
		"!#\7+\2\2\"!\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7 \2\2%\5\3\2\2\2&)\5\n\6"+
		"\2\')\5\b\5\2(&\3\2\2\2(\'\3\2\2\2)\61\3\2\2\2*-\7\"\2\2+.\5\n\6\2,.\5"+
		"\b\5\2-+\3\2\2\2-,\3\2\2\2.\60\3\2\2\2/*\3\2\2\2\60\63\3\2\2\2\61/\3\2"+
		"\2\2\61\62\3\2\2\2\62\7\3\2\2\2\63\61\3\2\2\2\64\67\5\20\t\2\65\67\5\22"+
		"\n\2\66\64\3\2\2\2\66\65\3\2\2\2\67\t\3\2\2\28;\5\f\7\29;\5\16\b\2:8\3"+
		"\2\2\2:9\3\2\2\2;\13\3\2\2\2<=\5\20\t\2=>\7+\2\2>?\5\24\13\2?\r\3\2\2"+
		"\2@A\5\22\n\2AB\7+\2\2BC\5\24\13\2C\17\3\2\2\2DE\7\31\2\2E\21\3\2\2\2"+
		"FJ\7\31\2\2GH\7\34\2\2HI\7$\2\2IK\7\35\2\2JG\3\2\2\2KL\3\2\2\2LJ\3\2\2"+
		"\2LM\3\2\2\2M\23\3\2\2\2NS\7$\2\2OS\7%\2\2PS\7&\2\2QS\5\32\16\2RN\3\2"+
		"\2\2RO\3\2\2\2RP\3\2\2\2RQ\3\2\2\2S\25\3\2\2\2TY\7$\2\2UV\7\"\2\2VX\7"+
		"$\2\2WU\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\27\3\2\2\2[Y\3\2\2\2\\"+
		"a\7%\2\2]^\7\"\2\2^`\7%\2\2_]\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\31"+
		"\3\2\2\2ca\3\2\2\2dh\7\32\2\2ei\5\32\16\2fi\5\26\f\2gi\5\30\r\2he\3\2"+
		"\2\2hf\3\2\2\2hg\3\2\2\2in\3\2\2\2jk\7\"\2\2km\5\32\16\2lj\3\2\2\2mp\3"+
		"\2\2\2nl\3\2\2\2no\3\2\2\2oq\3\2\2\2pn\3\2\2\2qr\7\33\2\2r\33\3\2\2\2"+
		"\16\"(-\61\66:LRYahn";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}