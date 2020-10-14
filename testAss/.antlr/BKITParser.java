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
		INTEGER=34, FLOAT=35, BOLEAN=36, FADDOP=37, IADDOP=38, FSUBOP=39, ISUBOP=40, 
		FMULOP=41, IMULOP=42, FDIVOP=43, IDIVOP=44, IREMAIN=45, EQUAL=46, FNEQUAL=47, 
		FLESSOE=48, FGROE=49, FLESS=50, FGR=51, INEQUAL=52, ILESSOE=53, IGROE=54, 
		ILESS=55, IGR=56, BNEG=57, BAND=58, BOR=59, AS=60;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_var_list = 2, RULE_func_declare = 3, 
		RULE_func_body = 4, RULE_stm_list = 5, RULE_stm = 6, RULE_non_initted_var = 7, 
		RULE_initted_var = 8, RULE_scalar_init = 9, RULE_composite_init = 10, 
		RULE_scalar_var = 11, RULE_composite_var = 12, RULE_para_list = 13, RULE_assign_stm = 14, 
		RULE_expression = 15, RULE_literals = 16, RULE_int_array = 17, RULE_float_array = 18, 
		RULE_array_list = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "func_declare", "func_body", "stm_list", 
			"stm", "non_initted_var", "initted_var", "scalar_init", "composite_init", 
			"scalar_var", "composite_var", "para_list", "assign_stm", "expression", 
			"literals", "int_array", "float_array", "array_list"
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
			setState(40);
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
			setState(42);
			match(VAR);
			setState(43);
			match(COLON);
			setState(44);
			var_list();
			setState(46);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(45);
				match(AS);
				}
			}

			setState(48);
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
			setState(52);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(50);
				initted_var();
				}
				break;
			case 2:
				{
				setState(51);
				non_initted_var();
				}
				break;
			}
			setState(61);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(54);
				match(CM);
				setState(57);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(55);
					initted_var();
					}
					break;
				case 2:
					{
					setState(56);
					non_initted_var();
					}
					break;
				}
				}
				}
				setState(63);
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

	public static class Func_declareContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public List<TerminalNode> COLON() { return getTokens(BKITParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BKITParser.COLON, i);
		}
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public Func_bodyContext func_body() {
			return getRuleContext(Func_bodyContext.class,0);
		}
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public Para_listContext para_list() {
			return getRuleContext(Para_listContext.class,0);
		}
		public Func_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_declare; }
	}

	public final Func_declareContext func_declare() throws RecognitionException {
		Func_declareContext _localctx = new Func_declareContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_func_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(FUNCTION);
			setState(65);
			match(COLON);
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(66);
				match(PARAMETER);
				setState(67);
				match(COLON);
				setState(68);
				para_list();
				}
			}

			setState(71);
			match(BODY);
			setState(72);
			func_body();
			setState(73);
			match(ENDBODY);
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

	public static class Func_bodyContext extends ParserRuleContext {
		public Stm_listContext stm_list() {
			return getRuleContext(Stm_listContext.class,0);
		}
		public Func_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_body; }
	}

	public final Func_bodyContext func_body() throws RecognitionException {
		Func_bodyContext _localctx = new Func_bodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_func_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			stm_list();
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

	public static class Stm_listContext extends ParserRuleContext {
		public List<StmContext> stm() {
			return getRuleContexts(StmContext.class);
		}
		public StmContext stm(int i) {
			return getRuleContext(StmContext.class,i);
		}
		public Stm_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stm_list; }
	}

	public final Stm_listContext stm_list() throws RecognitionException {
		Stm_listContext _localctx = new Stm_listContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_stm_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(77);
				stm();
				}
				}
				setState(80); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==VAR );
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

	public static class StmContext extends ParserRuleContext {
		public Var_declareContext var_declare() {
			return getRuleContext(Var_declareContext.class,0);
		}
		public StmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stm; }
	}

	public final StmContext stm() throws RecognitionException {
		StmContext _localctx = new StmContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
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
		enterRule(_localctx, 14, RULE_non_initted_var);
		try {
			setState(86);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				scalar_var();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
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
		enterRule(_localctx, 16, RULE_initted_var);
		try {
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				scalar_init();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
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
		enterRule(_localctx, 18, RULE_scalar_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			scalar_var();
			setState(93);
			match(AS);
			setState(94);
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
		enterRule(_localctx, 20, RULE_composite_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			composite_var();
			setState(97);
			match(AS);
			setState(98);
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
		enterRule(_localctx, 22, RULE_scalar_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
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
		enterRule(_localctx, 24, RULE_composite_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(IDENTIFIER);
			setState(106); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(103);
				match(LK);
				setState(104);
				match(INTEGER);
				setState(105);
				match(RK);
				}
				}
				setState(108); 
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

	public static class Para_listContext extends ParserRuleContext {
		public List<TerminalNode> IDENTIFIER() { return getTokens(BKITParser.IDENTIFIER); }
		public TerminalNode IDENTIFIER(int i) {
			return getToken(BKITParser.IDENTIFIER, i);
		}
		public TerminalNode CM() { return getToken(BKITParser.CM, 0); }
		public Para_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para_list; }
	}

	public final Para_listContext para_list() throws RecognitionException {
		Para_listContext _localctx = new Para_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_para_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(IDENTIFIER);
			{
			setState(111);
			match(CM);
			setState(112);
			match(IDENTIFIER);
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

	public static class Assign_stmContext extends ParserRuleContext {
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public Composite_varContext composite_var() {
			return getRuleContext(Composite_varContext.class,0);
		}
		public Assign_stmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stm; }
	}

	public final Assign_stmContext assign_stm() throws RecognitionException {
		Assign_stmContext _localctx = new Assign_stmContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_assign_stm);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(114);
				scalar_var();
				}
				break;
			case 2:
				{
				setState(115);
				composite_var();
				}
				break;
			}
			setState(118);
			match(AS);
			setState(119);
			expression();
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

	public static class ExpressionContext extends ParserRuleContext {
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expression);
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
		enterRule(_localctx, 32, RULE_literals);
		try {
			setState(127);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(123);
				match(INTEGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(124);
				match(FLOAT);
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 3);
				{
				setState(125);
				match(BOLEAN);
				}
				break;
			case LB:
				enterOuterAlt(_localctx, 4);
				{
				setState(126);
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
		enterRule(_localctx, 34, RULE_int_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(INTEGER);
			setState(134);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(130);
					match(CM);
					setState(131);
					match(INTEGER);
					}
					} 
				}
				setState(136);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
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
		enterRule(_localctx, 36, RULE_float_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(FLOAT);
			setState(142);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(138);
					match(CM);
					setState(139);
					match(FLOAT);
					}
					} 
				}
				setState(144);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
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
		enterRule(_localctx, 38, RULE_array_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			match(LB);
			setState(149);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				{
				setState(146);
				array_list();
				}
				break;
			case INTEGER:
				{
				setState(147);
				int_array();
				}
				break;
			case FLOAT:
				{
				setState(148);
				float_array();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(151);
				match(CM);
				setState(152);
				array_list();
				}
				}
				setState(157);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(158);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>\u00a3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\3\3\3\5\3\61\n\3\3\3"+
		"\3\3\3\4\3\4\5\4\67\n\4\3\4\3\4\3\4\5\4<\n\4\7\4>\n\4\f\4\16\4A\13\4\3"+
		"\5\3\5\3\5\3\5\3\5\5\5H\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\6\7Q\n\7\r\7\16"+
		"\7R\3\b\3\b\3\t\3\t\5\tY\n\t\3\n\3\n\5\n]\n\n\3\13\3\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\6\16m\n\16\r\16\16\16n\3\17\3"+
		"\17\3\17\3\17\3\20\3\20\5\20w\n\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22"+
		"\3\22\3\22\5\22\u0082\n\22\3\23\3\23\3\23\7\23\u0087\n\23\f\23\16\23\u008a"+
		"\13\23\3\24\3\24\3\24\7\24\u008f\n\24\f\24\16\24\u0092\13\24\3\25\3\25"+
		"\3\25\3\25\5\25\u0098\n\25\3\25\3\25\7\25\u009c\n\25\f\25\16\25\u009f"+
		"\13\25\3\25\3\25\3\25\2\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \""+
		"$&(\2\2\2\u00a0\2*\3\2\2\2\4,\3\2\2\2\6\66\3\2\2\2\bB\3\2\2\2\nM\3\2\2"+
		"\2\fP\3\2\2\2\16T\3\2\2\2\20X\3\2\2\2\22\\\3\2\2\2\24^\3\2\2\2\26b\3\2"+
		"\2\2\30f\3\2\2\2\32h\3\2\2\2\34p\3\2\2\2\36v\3\2\2\2 {\3\2\2\2\"\u0081"+
		"\3\2\2\2$\u0083\3\2\2\2&\u008b\3\2\2\2(\u0093\3\2\2\2*+\5\4\3\2+\3\3\2"+
		"\2\2,-\7\3\2\2-.\7!\2\2.\60\5\6\4\2/\61\7>\2\2\60/\3\2\2\2\60\61\3\2\2"+
		"\2\61\62\3\2\2\2\62\63\7 \2\2\63\5\3\2\2\2\64\67\5\22\n\2\65\67\5\20\t"+
		"\2\66\64\3\2\2\2\66\65\3\2\2\2\67?\3\2\2\28;\7\"\2\29<\5\22\n\2:<\5\20"+
		"\t\2;9\3\2\2\2;:\3\2\2\2<>\3\2\2\2=8\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2"+
		"\2\2@\7\3\2\2\2A?\3\2\2\2BC\7\4\2\2CG\7!\2\2DE\7\r\2\2EF\7!\2\2FH\5\34"+
		"\17\2GD\3\2\2\2GH\3\2\2\2HI\3\2\2\2IJ\7\5\2\2JK\5\n\6\2KL\7\20\2\2L\t"+
		"\3\2\2\2MN\5\f\7\2N\13\3\2\2\2OQ\5\16\b\2PO\3\2\2\2QR\3\2\2\2RP\3\2\2"+
		"\2RS\3\2\2\2S\r\3\2\2\2TU\5\4\3\2U\17\3\2\2\2VY\5\30\r\2WY\5\32\16\2X"+
		"V\3\2\2\2XW\3\2\2\2Y\21\3\2\2\2Z]\5\24\13\2[]\5\26\f\2\\Z\3\2\2\2\\[\3"+
		"\2\2\2]\23\3\2\2\2^_\5\30\r\2_`\7>\2\2`a\5\"\22\2a\25\3\2\2\2bc\5\32\16"+
		"\2cd\7>\2\2de\5\"\22\2e\27\3\2\2\2fg\7\31\2\2g\31\3\2\2\2hl\7\31\2\2i"+
		"j\7\34\2\2jk\7$\2\2km\7\35\2\2li\3\2\2\2mn\3\2\2\2nl\3\2\2\2no\3\2\2\2"+
		"o\33\3\2\2\2pq\7\31\2\2qr\7\"\2\2rs\7\31\2\2s\35\3\2\2\2tw\5\30\r\2uw"+
		"\5\32\16\2vt\3\2\2\2vu\3\2\2\2wx\3\2\2\2xy\7>\2\2yz\5 \21\2z\37\3\2\2"+
		"\2{|\3\2\2\2|!\3\2\2\2}\u0082\7$\2\2~\u0082\7%\2\2\177\u0082\7&\2\2\u0080"+
		"\u0082\5(\25\2\u0081}\3\2\2\2\u0081~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080"+
		"\3\2\2\2\u0082#\3\2\2\2\u0083\u0088\7$\2\2\u0084\u0085\7\"\2\2\u0085\u0087"+
		"\7$\2\2\u0086\u0084\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088"+
		"\u0089\3\2\2\2\u0089%\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u0090\7%\2\2\u008c"+
		"\u008d\7\"\2\2\u008d\u008f\7%\2\2\u008e\u008c\3\2\2\2\u008f\u0092\3\2"+
		"\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\'\3\2\2\2\u0092\u0090"+
		"\3\2\2\2\u0093\u0097\7\32\2\2\u0094\u0098\5(\25\2\u0095\u0098\5$\23\2"+
		"\u0096\u0098\5&\24\2\u0097\u0094\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096"+
		"\3\2\2\2\u0098\u009d\3\2\2\2\u0099\u009a\7\"\2\2\u009a\u009c\5(\25\2\u009b"+
		"\u0099\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2"+
		"\2\2\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7\33\2\2\u00a1"+
		")\3\2\2\2\21\60\66;?GRX\\nv\u0081\u0088\u0090\u0097\u009d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}