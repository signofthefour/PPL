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
		WS=1, COMMENT=2, RELATION_OP=3, ADDSUB=4, MULDIV=5, NEGSIGN=6, IDENTIFIER=7, 
		LB=8, RB=9, LK=10, RK=11, LP=12, RP=13, SEMI=14, COLON=15, CM=16, DOT=17, 
		INTEGER=18, FLOAT=19, BOLEAN=20, FADDOP=21, IADDOP=22, FSUBOP=23, ISUBOP=24, 
		FMULOP=25, IMULOP=26, FDIVOP=27, IDIVOP=28, IREMAIN=29, EQUAL=30, FNEQUAL=31, 
		FLESSOE=32, FGROE=33, FLESS=34, FGR=35, INEQUAL=36, ILESSOE=37, IGROE=38, 
		ILESS=39, IGR=40, BNEG=41, BAND=42, BOR=43, AS=44, VAR=45, FUNCTION=46, 
		BODY=47, ELSE=48, ENDFOR=49, IF=50, ENDDO=51, BREAK=52, ELSEIF=53, ENDWHILE=54, 
		PARAMETER=55, WHILE=56, CONTINUE=57, ENDBODY=58, FOR=59, RETURN=60, TRUE=61, 
		DO=62, ENDIF=63, THEN=64, FALSE=65, ERROR_CHAR=66, UNCLOSE_STRING=67, 
		ILLEGAL_ESCAPE=68, UNTERMINATED_COMMENT=69, LSTRING=70;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_var_list = 2, RULE_main_func = 3, 
		RULE_func_declare = 4, RULE_func_body = 5, RULE_stm_list = 6, RULE_stm = 7, 
		RULE_non_initted_var = 8, RULE_initted_var = 9, RULE_scalar_init = 10, 
		RULE_composite_init = 11, RULE_scalar_var = 12, RULE_composite_var = 13, 
		RULE_para_list = 14, RULE_if_stmt = 15, RULE_assign_stmt = 16, RULE_composite_ass = 17, 
		RULE_for_stmt = 18, RULE_while_stmt = 19, RULE_do_while_stmt = 20, RULE_break_stmt = 21, 
		RULE_continue_stmt = 22, RULE_return_stmt = 23, RULE_func_call = 24, RULE_call_stmt = 25, 
		RULE_index_op = 26, RULE_expression = 27, RULE_exp0 = 28, RULE_exp1 = 29, 
		RULE_exp2 = 30, RULE_exp3 = 31, RULE_exp4 = 32, RULE_exp5 = 33, RULE_exp6 = 34, 
		RULE_exp7 = 35, RULE_exp8 = 36, RULE_operand = 37, RULE_literals = 38, 
		RULE_int_array = 39, RULE_float_array = 40, RULE_string_array = 41, RULE_array_index = 42, 
		RULE_array_list = 43;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "main_func", "func_declare", "func_body", 
			"stm_list", "stm", "non_initted_var", "initted_var", "scalar_init", "composite_init", 
			"scalar_var", "composite_var", "para_list", "if_stmt", "assign_stmt", 
			"composite_ass", "for_stmt", "while_stmt", "do_while_stmt", "break_stmt", 
			"continue_stmt", "return_stmt", "func_call", "call_stmt", "index_op", 
			"expression", "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
			"exp7", "exp8", "operand", "literals", "int_array", "float_array", "string_array", 
			"array_index", "array_list"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "'{'", "'}'", "'['", 
			"']'", "'('", "')'", "';'", "':'", "','", "'.'", null, null, null, "'+.'", 
			"'+'", "'-.'", "'-'", "'*.'", "'*'", "'\\.'", "'\\'", "'%'", "'=='", 
			"'=/='", "'<=.'", "'>=.'", "'<.'", "'>.'", "'!='", "'<='", "'>='", "'<'", 
			"'>'", "'!'", "'&&'", "'||'", "'='", "'Var'", "'Function'", "'Body'", 
			"'Else'", "'EndFor'", "'If'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", 
			"'Parameter'", "'While'", "'Continue'", "'EndBody'", "'For'", "'Return'", 
			"'True'", "'Do'", "'EndIf'", "'Then'", "'False'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "COMMENT", "RELATION_OP", "ADDSUB", "MULDIV", "NEGSIGN", 
			"IDENTIFIER", "LB", "RB", "LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", 
			"DOT", "INTEGER", "FLOAT", "BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", 
			"FMULOP", "IMULOP", "FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", 
			"FLESSOE", "FGROE", "FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", 
			"IGR", "BNEG", "BAND", "BOR", "AS", "VAR", "FUNCTION", "BODY", "ELSE", 
			"ENDFOR", "IF", "ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", 
			"WHILE", "CONTINUE", "ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", 
			"THEN", "FALSE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
			"LSTRING"
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
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public List<Func_declareContext> func_declare() {
			return getRuleContexts(Func_declareContext.class);
		}
		public Func_declareContext func_declare(int i) {
			return getRuleContext(Func_declareContext.class,i);
		}
		public List<Var_declareContext> var_declare() {
			return getRuleContexts(Var_declareContext.class);
		}
		public Var_declareContext var_declare(int i) {
			return getRuleContext(Var_declareContext.class,i);
		}
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(88);
				var_declare();
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(94);
				func_declare();
				}
				}
				setState(99);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(100);
			match(EOF);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVar_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVar_declare(this);
		}
	}

	public final Var_declareContext var_declare() throws RecognitionException {
		Var_declareContext _localctx = new Var_declareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(VAR);
			setState(103);
			match(COLON);
			setState(104);
			var_list();
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(105);
				match(AS);
				}
			}

			setState(108);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVar_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVar_list(this);
		}
	}

	public final Var_listContext var_list() throws RecognitionException {
		Var_listContext _localctx = new Var_listContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_var_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(110);
				initted_var();
				}
				break;
			case 2:
				{
				setState(111);
				non_initted_var();
				}
				break;
			}
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(114);
				match(CM);
				setState(117);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
				case 1:
					{
					setState(115);
					initted_var();
					}
					break;
				case 2:
					{
					setState(116);
					non_initted_var();
					}
					break;
				}
				}
				}
				setState(123);
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

	public static class Main_funcContext extends ParserRuleContext {
		public Main_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterMain_func(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitMain_func(this);
		}
	}

	public final Main_funcContext main_func() throws RecognitionException {
		Main_funcContext _localctx = new Main_funcContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_main_func);
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

	public static class Func_declareContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public List<TerminalNode> COLON() { return getTokens(BKITParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BKITParser.COLON, i);
		}
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public Func_bodyContext func_body() {
			return getRuleContext(Func_bodyContext.class,0);
		}
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public Para_listContext para_list() {
			return getRuleContext(Para_listContext.class,0);
		}
		public Func_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunc_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunc_declare(this);
		}
	}

	public final Func_declareContext func_declare() throws RecognitionException {
		Func_declareContext _localctx = new Func_declareContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_func_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(FUNCTION);
			setState(127);
			match(COLON);
			setState(128);
			match(IDENTIFIER);
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(129);
				match(PARAMETER);
				setState(130);
				match(COLON);
				setState(131);
				para_list();
				}
			}

			setState(134);
			match(BODY);
			setState(135);
			match(COLON);
			setState(136);
			func_body();
			setState(137);
			match(ENDBODY);
			setState(138);
			match(DOT);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunc_body(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunc_body(this);
		}
	}

	public final Func_bodyContext func_body() throws RecognitionException {
		Func_bodyContext _localctx = new Func_bodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_func_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStm_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStm_list(this);
		}
	}

	public final Stm_listContext stm_list() throws RecognitionException {
		Stm_listContext _localctx = new Stm_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_stm_list);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(142);
					stm();
					}
					} 
				}
				setState(147);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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

	public static class StmContext extends ParserRuleContext {
		public Var_declareContext var_declare() {
			return getRuleContext(Var_declareContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public Do_while_stmtContext do_while_stmt() {
			return getRuleContext(Do_while_stmtContext.class,0);
		}
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Continue_stmtContext continue_stmt() {
			return getRuleContext(Continue_stmtContext.class,0);
		}
		public Call_stmtContext call_stmt() {
			return getRuleContext(Call_stmtContext.class,0);
		}
		public Return_stmtContext return_stmt() {
			return getRuleContext(Return_stmtContext.class,0);
		}
		public StmContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stm; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStm(this);
		}
	}

	public final StmContext stm() throws RecognitionException {
		StmContext _localctx = new StmContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_stm);
		try {
			setState(158);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(148);
				var_declare();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(149);
				assign_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(150);
				if_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(151);
				for_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(152);
				while_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(153);
				do_while_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(154);
				break_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(155);
				continue_stmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(156);
				call_stmt();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(157);
				return_stmt();
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterNon_initted_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitNon_initted_var(this);
		}
	}

	public final Non_initted_varContext non_initted_var() throws RecognitionException {
		Non_initted_varContext _localctx = new Non_initted_varContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_non_initted_var);
		try {
			setState(162);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(160);
				scalar_var();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(161);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterInitted_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitInitted_var(this);
		}
	}

	public final Initted_varContext initted_var() throws RecognitionException {
		Initted_varContext _localctx = new Initted_varContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_initted_var);
		try {
			setState(166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(164);
				scalar_init();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(165);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterScalar_init(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitScalar_init(this);
		}
	}

	public final Scalar_initContext scalar_init() throws RecognitionException {
		Scalar_initContext _localctx = new Scalar_initContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_scalar_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			scalar_var();
			setState(169);
			match(AS);
			setState(170);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterComposite_init(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitComposite_init(this);
		}
	}

	public final Composite_initContext composite_init() throws RecognitionException {
		Composite_initContext _localctx = new Composite_initContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_composite_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			composite_var();
			setState(173);
			match(AS);
			setState(174);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterScalar_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitScalar_var(this);
		}
	}

	public final Scalar_varContext scalar_var() throws RecognitionException {
		Scalar_varContext _localctx = new Scalar_varContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_scalar_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterComposite_var(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitComposite_var(this);
		}
	}

	public final Composite_varContext composite_var() throws RecognitionException {
		Composite_varContext _localctx = new Composite_varContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_composite_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(178);
			match(IDENTIFIER);
			setState(182); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(179);
				match(LK);
				setState(180);
				match(INTEGER);
				setState(181);
				match(RK);
				}
				}
				setState(184); 
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
		public List<Scalar_varContext> scalar_var() {
			return getRuleContexts(Scalar_varContext.class);
		}
		public Scalar_varContext scalar_var(int i) {
			return getRuleContext(Scalar_varContext.class,i);
		}
		public List<Composite_varContext> composite_var() {
			return getRuleContexts(Composite_varContext.class);
		}
		public Composite_varContext composite_var(int i) {
			return getRuleContext(Composite_varContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Para_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterPara_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitPara_list(this);
		}
	}

	public final Para_listContext para_list() throws RecognitionException {
		Para_listContext _localctx = new Para_listContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_para_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(186);
				scalar_var();
				}
				break;
			case 2:
				{
				setState(187);
				composite_var();
				}
				break;
			}
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(190);
				match(CM);
				setState(193);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
				case 1:
					{
					setState(191);
					scalar_var();
					}
					break;
				case 2:
					{
					setState(192);
					composite_var();
					}
					break;
				}
				}
				}
				setState(199);
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

	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKITParser.IF, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> THEN() { return getTokens(BKITParser.THEN); }
		public TerminalNode THEN(int i) {
			return getToken(BKITParser.THEN, i);
		}
		public List<Stm_listContext> stm_list() {
			return getRuleContexts(Stm_listContext.class);
		}
		public Stm_listContext stm_list(int i) {
			return getRuleContext(Stm_listContext.class,i);
		}
		public TerminalNode ENDIF() { return getToken(BKITParser.ENDIF, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public List<TerminalNode> ELSEIF() { return getTokens(BKITParser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(BKITParser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(BKITParser.ELSE, 0); }
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIf_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIf_stmt(this);
		}
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(IF);
			setState(201);
			expression();
			setState(202);
			match(THEN);
			setState(203);
			stm_list();
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(204);
				match(ELSEIF);
				setState(205);
				expression();
				setState(206);
				match(THEN);
				setState(207);
				stm_list();
				}
				}
				setState(213);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(214);
				match(ELSE);
				setState(215);
				stm_list();
				}
			}

			setState(218);
			match(ENDIF);
			setState(219);
			match(DOT);
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

	public static class Assign_stmtContext extends ParserRuleContext {
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Scalar_varContext scalar_var() {
			return getRuleContext(Scalar_varContext.class,0);
		}
		public Composite_assContext composite_ass() {
			return getRuleContext(Composite_assContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterAssign_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitAssign_stmt(this);
		}
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(221);
				scalar_var();
				}
				break;
			case 2:
				{
				setState(222);
				composite_ass();
				}
				break;
			}
			setState(225);
			match(AS);
			setState(226);
			expression();
			setState(227);
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

	public static class Composite_assContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Composite_assContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_composite_ass; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterComposite_ass(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitComposite_ass(this);
		}
	}

	public final Composite_assContext composite_ass() throws RecognitionException {
		Composite_assContext _localctx = new Composite_assContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_composite_ass);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(IDENTIFIER);
			setState(230);
			index_op();
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

	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKITParser.FOR, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public List<Scalar_varContext> scalar_var() {
			return getRuleContexts(Scalar_varContext.class);
		}
		public Scalar_varContext scalar_var(int i) {
			return getRuleContext(Scalar_varContext.class,i);
		}
		public List<TerminalNode> AS() { return getTokens(BKITParser.AS); }
		public TerminalNode AS(int i) {
			return getToken(BKITParser.AS, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stm_listContext stm_list() {
			return getRuleContext(Stm_listContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(BKITParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFor_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFor_stmt(this);
		}
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(FOR);
			setState(233);
			match(LP);
			setState(234);
			scalar_var();
			setState(235);
			match(AS);
			setState(236);
			expression();
			setState(237);
			match(CM);
			setState(238);
			expression();
			setState(239);
			match(CM);
			setState(245);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				{
				{
				setState(240);
				scalar_var();
				setState(241);
				match(AS);
				setState(242);
				expression();
				}
				}
				break;
			case LB:
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case LSTRING:
				{
				setState(244);
				literals();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(247);
			match(RP);
			setState(248);
			match(DO);
			setState(249);
			stm_list();
			setState(250);
			match(ENDFOR);
			setState(251);
			match(DOT);
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

	public static class While_stmtContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stm_listContext stm_list() {
			return getRuleContext(Stm_listContext.class,0);
		}
		public TerminalNode ENDWHILE() { return getToken(BKITParser.ENDWHILE, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public While_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterWhile_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitWhile_stmt(this);
		}
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(WHILE);
			setState(254);
			expression();
			setState(255);
			match(DO);
			setState(256);
			stm_list();
			setState(257);
			match(ENDWHILE);
			setState(258);
			match(DOT);
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

	public static class Do_while_stmtContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stm_listContext stm_list() {
			return getRuleContext(Stm_listContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode ENDDO() { return getToken(BKITParser.ENDDO, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public Do_while_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterDo_while_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitDo_while_stmt(this);
		}
	}

	public final Do_while_stmtContext do_while_stmt() throws RecognitionException {
		Do_while_stmtContext _localctx = new Do_while_stmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_do_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(DO);
			setState(261);
			stm_list();
			setState(262);
			match(WHILE);
			setState(263);
			expression();
			setState(264);
			match(ENDDO);
			setState(265);
			match(DOT);
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

	public static class Break_stmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(BKITParser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterBreak_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitBreak_stmt(this);
		}
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(BREAK);
			setState(268);
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

	public static class Continue_stmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(BKITParser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Continue_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterContinue_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitContinue_stmt(this);
		}
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(CONTINUE);
			setState(271);
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

	public static class Return_stmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(BKITParser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterReturn_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitReturn_stmt(this);
		}
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			match(RETURN);
			setState(282);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDSUB) | (1L << IDENTIFIER) | (1L << LB) | (1L << LP) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOLEAN) | (1L << BNEG))) != 0) || _la==LSTRING) {
				{
				setState(274);
				expression();
				setState(279);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(275);
					match(CM);
					setState(276);
					expression();
					}
					}
					setState(281);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(284);
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

	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunc_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunc_call(this);
		}
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
			match(IDENTIFIER);
			setState(287);
			match(LP);
			setState(296);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDSUB) | (1L << IDENTIFIER) | (1L << LB) | (1L << LP) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOLEAN) | (1L << BNEG))) != 0) || _la==LSTRING) {
				{
				setState(288);
				expression();
				setState(293);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(289);
					match(CM);
					setState(290);
					expression();
					}
					}
					setState(295);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(298);
			match(RP);
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

	public static class Call_stmtContext extends ParserRuleContext {
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
		public Call_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterCall_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitCall_stmt(this);
		}
	}

	public final Call_stmtContext call_stmt() throws RecognitionException {
		Call_stmtContext _localctx = new Call_stmtContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			func_call();
			setState(301);
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

	public static class Index_opContext extends ParserRuleContext {
		public List<TerminalNode> LK() { return getTokens(BKITParser.LK); }
		public TerminalNode LK(int i) {
			return getToken(BKITParser.LK, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> RK() { return getTokens(BKITParser.RK); }
		public TerminalNode RK(int i) {
			return getToken(BKITParser.RK, i);
		}
		public Index_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIndex_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIndex_op(this);
		}
	}

	public final Index_opContext index_op() throws RecognitionException {
		Index_opContext _localctx = new Index_opContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_index_op);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(307); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(303);
					match(LK);
					setState(304);
					expression();
					setState(305);
					match(RK);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(309); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
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
		public Exp0Context exp0() {
			return getRuleContext(Exp0Context.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			exp0(0);
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

	public static class Exp0Context extends ParserRuleContext {
		public Exp1Context exp1() {
			return getRuleContext(Exp1Context.class,0);
		}
		public List<Exp0Context> exp0() {
			return getRuleContexts(Exp0Context.class);
		}
		public Exp0Context exp0(int i) {
			return getRuleContext(Exp0Context.class,i);
		}
		public TerminalNode RELATION_OP() { return getToken(BKITParser.RELATION_OP, 0); }
		public Exp0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp0; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp0(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp0(this);
		}
	}

	public final Exp0Context exp0() throws RecognitionException {
		return exp0(0);
	}

	private Exp0Context exp0(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp0Context _localctx = new Exp0Context(_ctx, _parentState);
		Exp0Context _prevctx = _localctx;
		int _startState = 56;
		enterRecursionRule(_localctx, 56, RULE_exp0, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(314);
			exp1(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(321);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp0Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp0);
					setState(316);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(317);
					match(RELATION_OP);
					setState(318);
					exp0(3);
					}
					} 
				}
				setState(323);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp1Context extends ParserRuleContext {
		public Exp2Context exp2() {
			return getRuleContext(Exp2Context.class,0);
		}
		public Exp1Context exp1() {
			return getRuleContext(Exp1Context.class,0);
		}
		public TerminalNode BAND() { return getToken(BKITParser.BAND, 0); }
		public TerminalNode BOR() { return getToken(BKITParser.BOR, 0); }
		public Exp1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp1(this);
		}
	}

	public final Exp1Context exp1() throws RecognitionException {
		return exp1(0);
	}

	private Exp1Context exp1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp1Context _localctx = new Exp1Context(_ctx, _parentState);
		Exp1Context _prevctx = _localctx;
		int _startState = 58;
		enterRecursionRule(_localctx, 58, RULE_exp1, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(325);
			exp2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(332);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp1);
					setState(327);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(328);
					_la = _input.LA(1);
					if ( !(_la==BAND || _la==BOR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(329);
					exp2(0);
					}
					} 
				}
				setState(334);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp2Context extends ParserRuleContext {
		public Exp3Context exp3() {
			return getRuleContext(Exp3Context.class,0);
		}
		public Exp2Context exp2() {
			return getRuleContext(Exp2Context.class,0);
		}
		public TerminalNode ADDSUB() { return getToken(BKITParser.ADDSUB, 0); }
		public Exp2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp2(this);
		}
	}

	public final Exp2Context exp2() throws RecognitionException {
		return exp2(0);
	}

	private Exp2Context exp2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp2Context _localctx = new Exp2Context(_ctx, _parentState);
		Exp2Context _prevctx = _localctx;
		int _startState = 60;
		enterRecursionRule(_localctx, 60, RULE_exp2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(336);
			exp3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(343);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp2);
					setState(338);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(339);
					match(ADDSUB);
					}
					setState(340);
					exp3(0);
					}
					} 
				}
				setState(345);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,26,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp3Context extends ParserRuleContext {
		public Exp4Context exp4() {
			return getRuleContext(Exp4Context.class,0);
		}
		public Exp3Context exp3() {
			return getRuleContext(Exp3Context.class,0);
		}
		public TerminalNode MULDIV() { return getToken(BKITParser.MULDIV, 0); }
		public Exp3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp3(this);
		}
	}

	public final Exp3Context exp3() throws RecognitionException {
		return exp3(0);
	}

	private Exp3Context exp3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp3Context _localctx = new Exp3Context(_ctx, _parentState);
		Exp3Context _prevctx = _localctx;
		int _startState = 62;
		enterRecursionRule(_localctx, 62, RULE_exp3, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(347);
			exp4();
			}
			_ctx.stop = _input.LT(-1);
			setState(354);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp3);
					setState(349);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(350);
					match(MULDIV);
					}
					setState(351);
					exp4();
					}
					} 
				}
				setState(356);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,27,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp4Context extends ParserRuleContext {
		public TerminalNode BNEG() { return getToken(BKITParser.BNEG, 0); }
		public Exp4Context exp4() {
			return getRuleContext(Exp4Context.class,0);
		}
		public Exp5Context exp5() {
			return getRuleContext(Exp5Context.class,0);
		}
		public Exp4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp4; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp4(this);
		}
	}

	public final Exp4Context exp4() throws RecognitionException {
		Exp4Context _localctx = new Exp4Context(_ctx, getState());
		enterRule(_localctx, 64, RULE_exp4);
		try {
			setState(360);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BNEG:
				enterOuterAlt(_localctx, 1);
				{
				setState(357);
				match(BNEG);
				setState(358);
				exp4();
				}
				break;
			case ADDSUB:
			case IDENTIFIER:
			case LB:
			case LP:
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case LSTRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(359);
				exp5();
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

	public static class Exp5Context extends ParserRuleContext {
		public TerminalNode ADDSUB() { return getToken(BKITParser.ADDSUB, 0); }
		public Exp5Context exp5() {
			return getRuleContext(Exp5Context.class,0);
		}
		public Exp6Context exp6() {
			return getRuleContext(Exp6Context.class,0);
		}
		public Exp5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp5; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp5(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp5(this);
		}
	}

	public final Exp5Context exp5() throws RecognitionException {
		Exp5Context _localctx = new Exp5Context(_ctx, getState());
		enterRule(_localctx, 66, RULE_exp5);
		try {
			setState(365);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADDSUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(362);
				match(ADDSUB);
				setState(363);
				exp5();
				}
				break;
			case IDENTIFIER:
			case LB:
			case LP:
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case LSTRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(364);
				exp6(0);
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

	public static class Exp6Context extends ParserRuleContext {
		public Exp7Context exp7() {
			return getRuleContext(Exp7Context.class,0);
		}
		public Exp6Context exp6() {
			return getRuleContext(Exp6Context.class,0);
		}
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Exp6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp6; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp6(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp6(this);
		}
	}

	public final Exp6Context exp6() throws RecognitionException {
		return exp6(0);
	}

	private Exp6Context exp6(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp6Context _localctx = new Exp6Context(_ctx, _parentState);
		Exp6Context _prevctx = _localctx;
		int _startState = 68;
		enterRecursionRule(_localctx, 68, RULE_exp6, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(368);
			exp7();
			}
			_ctx.stop = _input.LT(-1);
			setState(374);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp6Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp6);
					setState(370);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(371);
					index_op();
					}
					} 
				}
				setState(376);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp7Context extends ParserRuleContext {
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public Exp8Context exp8() {
			return getRuleContext(Exp8Context.class,0);
		}
		public Exp7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp7; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp7(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp7(this);
		}
	}

	public final Exp7Context exp7() throws RecognitionException {
		Exp7Context _localctx = new Exp7Context(_ctx, getState());
		enterRule(_localctx, 70, RULE_exp7);
		try {
			setState(379);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(377);
				func_call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(378);
				exp8();
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

	public static class Exp8Context extends ParserRuleContext {
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public Exp8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp8; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExp8(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExp8(this);
		}
	}

	public final Exp8Context exp8() throws RecognitionException {
		Exp8Context _localctx = new Exp8Context(_ctx, getState());
		enterRule(_localctx, 72, RULE_exp8);
		try {
			setState(386);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(381);
				match(LP);
				{
				setState(382);
				expression();
				}
				setState(383);
				match(RP);
				}
				break;
			case IDENTIFIER:
			case LB:
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case LSTRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(385);
				operand();
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

	public static class OperandContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
		public TerminalNode BOLEAN() { return getToken(BKITParser.BOLEAN, 0); }
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterOperand(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitOperand(this);
		}
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_operand);
		try {
			setState(391);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				match(IDENTIFIER);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				literals();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(390);
				match(BOLEAN);
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

	public static class LiteralsContext extends ParserRuleContext {
		public Array_listContext array_list() {
			return getRuleContext(Array_listContext.class,0);
		}
		public TerminalNode INTEGER() { return getToken(BKITParser.INTEGER, 0); }
		public TerminalNode FLOAT() { return getToken(BKITParser.FLOAT, 0); }
		public TerminalNode BOLEAN() { return getToken(BKITParser.BOLEAN, 0); }
		public TerminalNode LSTRING() { return getToken(BKITParser.LSTRING, 0); }
		public LiteralsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literals; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterLiterals(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitLiterals(this);
		}
	}

	public final LiteralsContext literals() throws RecognitionException {
		LiteralsContext _localctx = new LiteralsContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_literals);
		try {
			setState(398);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				setState(393);
				array_list();
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(394);
				match(INTEGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(395);
				match(FLOAT);
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 4);
				{
				setState(396);
				match(BOLEAN);
				}
				break;
			case LSTRING:
				enterOuterAlt(_localctx, 5);
				{
				setState(397);
				match(LSTRING);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterInt_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitInt_array(this);
		}
	}

	public final Int_arrayContext int_array() throws RecognitionException {
		Int_arrayContext _localctx = new Int_arrayContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_int_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(400);
			match(INTEGER);
			setState(405);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(401);
					match(CM);
					setState(402);
					match(INTEGER);
					}
					} 
				}
				setState(407);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFloat_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFloat_array(this);
		}
	}

	public final Float_arrayContext float_array() throws RecognitionException {
		Float_arrayContext _localctx = new Float_arrayContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_float_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(408);
			match(FLOAT);
			setState(413);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(409);
					match(CM);
					setState(410);
					match(FLOAT);
					}
					} 
				}
				setState(415);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
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

	public static class String_arrayContext extends ParserRuleContext {
		public List<TerminalNode> LSTRING() { return getTokens(BKITParser.LSTRING); }
		public TerminalNode LSTRING(int i) {
			return getToken(BKITParser.LSTRING, i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public String_arrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterString_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitString_array(this);
		}
	}

	public final String_arrayContext string_array() throws RecognitionException {
		String_arrayContext _localctx = new String_arrayContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_string_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(416);
			match(LSTRING);
			setState(421);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(417);
					match(CM);
					setState(418);
					match(LSTRING);
					}
					} 
				}
				setState(423);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
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

	public static class Array_indexContext extends ParserRuleContext {
		public Int_arrayContext int_array() {
			return getRuleContext(Int_arrayContext.class,0);
		}
		public Float_arrayContext float_array() {
			return getRuleContext(Float_arrayContext.class,0);
		}
		public String_arrayContext string_array() {
			return getRuleContext(String_arrayContext.class,0);
		}
		public Array_indexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_index; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray_index(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray_index(this);
		}
	}

	public final Array_indexContext array_index() throws RecognitionException {
		Array_indexContext _localctx = new Array_indexContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_array_index);
		try {
			setState(427);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(424);
				int_array();
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(425);
				float_array();
				}
				break;
			case LSTRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(426);
				string_array();
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
		public TerminalNode RB() { return getToken(BKITParser.RB, 0); }
		public List<Array_listContext> array_list() {
			return getRuleContexts(Array_listContext.class);
		}
		public Array_listContext array_list(int i) {
			return getRuleContext(Array_listContext.class,i);
		}
		public List<Array_indexContext> array_index() {
			return getRuleContexts(Array_indexContext.class);
		}
		public Array_indexContext array_index(int i) {
			return getRuleContext(Array_indexContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Array_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray_list(this);
		}
	}

	public final Array_listContext array_list() throws RecognitionException {
		Array_listContext _localctx = new Array_listContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_array_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(429);
			match(LB);
			setState(444);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & ((1L << (LB - 8)) | (1L << (INTEGER - 8)) | (1L << (FLOAT - 8)) | (1L << (LSTRING - 8)))) != 0)) {
				{
				setState(432);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LB:
					{
					setState(430);
					array_list();
					}
					break;
				case INTEGER:
				case FLOAT:
				case LSTRING:
					{
					setState(431);
					array_index();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(441);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(434);
					match(CM);
					setState(437);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LB:
						{
						setState(435);
						array_list();
						}
						break;
					case INTEGER:
					case FLOAT:
					case LSTRING:
						{
						setState(436);
						array_index();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					}
					setState(443);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(446);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 28:
			return exp0_sempred((Exp0Context)_localctx, predIndex);
		case 29:
			return exp1_sempred((Exp1Context)_localctx, predIndex);
		case 30:
			return exp2_sempred((Exp2Context)_localctx, predIndex);
		case 31:
			return exp3_sempred((Exp3Context)_localctx, predIndex);
		case 34:
			return exp6_sempred((Exp6Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp0_sempred(Exp0Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp1_sempred(Exp1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp2_sempred(Exp2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp3_sempred(Exp3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp6_sempred(Exp6Context _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H\u01c3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\3\2\7\2\\\n\2\f\2\16\2_\13\2\3\2\7\2b\n\2\f\2\16\2e\13\2\3"+
		"\2\3\2\3\3\3\3\3\3\3\3\5\3m\n\3\3\3\3\3\3\4\3\4\5\4s\n\4\3\4\3\4\3\4\5"+
		"\4x\n\4\7\4z\n\4\f\4\16\4}\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0087"+
		"\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\7\b\u0092\n\b\f\b\16\b\u0095"+
		"\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a1\n\t\3\n\3\n\5"+
		"\n\u00a5\n\n\3\13\3\13\5\13\u00a9\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r"+
		"\3\16\3\16\3\17\3\17\3\17\3\17\6\17\u00b9\n\17\r\17\16\17\u00ba\3\20\3"+
		"\20\5\20\u00bf\n\20\3\20\3\20\3\20\5\20\u00c4\n\20\7\20\u00c6\n\20\f\20"+
		"\16\20\u00c9\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00d4"+
		"\n\21\f\21\16\21\u00d7\13\21\3\21\3\21\5\21\u00db\n\21\3\21\3\21\3\21"+
		"\3\22\3\22\5\22\u00e2\n\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00f8\n\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31"+
		"\3\31\3\31\7\31\u0118\n\31\f\31\16\31\u011b\13\31\5\31\u011d\n\31\3\31"+
		"\3\31\3\32\3\32\3\32\3\32\3\32\7\32\u0126\n\32\f\32\16\32\u0129\13\32"+
		"\5\32\u012b\n\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\6\34\u0136"+
		"\n\34\r\34\16\34\u0137\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u0142"+
		"\n\36\f\36\16\36\u0145\13\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u014d"+
		"\n\37\f\37\16\37\u0150\13\37\3 \3 \3 \3 \3 \3 \7 \u0158\n \f \16 \u015b"+
		"\13 \3!\3!\3!\3!\3!\3!\7!\u0163\n!\f!\16!\u0166\13!\3\"\3\"\3\"\5\"\u016b"+
		"\n\"\3#\3#\3#\5#\u0170\n#\3$\3$\3$\3$\3$\7$\u0177\n$\f$\16$\u017a\13$"+
		"\3%\3%\5%\u017e\n%\3&\3&\3&\3&\3&\5&\u0185\n&\3\'\3\'\3\'\5\'\u018a\n"+
		"\'\3(\3(\3(\3(\3(\5(\u0191\n(\3)\3)\3)\7)\u0196\n)\f)\16)\u0199\13)\3"+
		"*\3*\3*\7*\u019e\n*\f*\16*\u01a1\13*\3+\3+\3+\7+\u01a6\n+\f+\16+\u01a9"+
		"\13+\3,\3,\3,\5,\u01ae\n,\3-\3-\3-\5-\u01b3\n-\3-\3-\3-\5-\u01b8\n-\7"+
		"-\u01ba\n-\f-\16-\u01bd\13-\5-\u01bf\n-\3-\3-\3-\2\7:<>@F.\2\4\6\b\n\f"+
		"\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX\2\3"+
		"\3\2,-\2\u01ce\2]\3\2\2\2\4h\3\2\2\2\6r\3\2\2\2\b~\3\2\2\2\n\u0080\3\2"+
		"\2\2\f\u008e\3\2\2\2\16\u0093\3\2\2\2\20\u00a0\3\2\2\2\22\u00a4\3\2\2"+
		"\2\24\u00a8\3\2\2\2\26\u00aa\3\2\2\2\30\u00ae\3\2\2\2\32\u00b2\3\2\2\2"+
		"\34\u00b4\3\2\2\2\36\u00be\3\2\2\2 \u00ca\3\2\2\2\"\u00e1\3\2\2\2$\u00e7"+
		"\3\2\2\2&\u00ea\3\2\2\2(\u00ff\3\2\2\2*\u0106\3\2\2\2,\u010d\3\2\2\2."+
		"\u0110\3\2\2\2\60\u0113\3\2\2\2\62\u0120\3\2\2\2\64\u012e\3\2\2\2\66\u0135"+
		"\3\2\2\28\u0139\3\2\2\2:\u013b\3\2\2\2<\u0146\3\2\2\2>\u0151\3\2\2\2@"+
		"\u015c\3\2\2\2B\u016a\3\2\2\2D\u016f\3\2\2\2F\u0171\3\2\2\2H\u017d\3\2"+
		"\2\2J\u0184\3\2\2\2L\u0189\3\2\2\2N\u0190\3\2\2\2P\u0192\3\2\2\2R\u019a"+
		"\3\2\2\2T\u01a2\3\2\2\2V\u01ad\3\2\2\2X\u01af\3\2\2\2Z\\\5\4\3\2[Z\3\2"+
		"\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^c\3\2\2\2_]\3\2\2\2`b\5\n\6\2a`\3"+
		"\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2df\3\2\2\2ec\3\2\2\2fg\7\2\2\3g\3"+
		"\3\2\2\2hi\7/\2\2ij\7\21\2\2jl\5\6\4\2km\7.\2\2lk\3\2\2\2lm\3\2\2\2mn"+
		"\3\2\2\2no\7\20\2\2o\5\3\2\2\2ps\5\24\13\2qs\5\22\n\2rp\3\2\2\2rq\3\2"+
		"\2\2s{\3\2\2\2tw\7\22\2\2ux\5\24\13\2vx\5\22\n\2wu\3\2\2\2wv\3\2\2\2x"+
		"z\3\2\2\2yt\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\7\3\2\2\2}{\3\2\2\2"+
		"~\177\3\2\2\2\177\t\3\2\2\2\u0080\u0081\7\60\2\2\u0081\u0082\7\21\2\2"+
		"\u0082\u0086\7\t\2\2\u0083\u0084\79\2\2\u0084\u0085\7\21\2\2\u0085\u0087"+
		"\5\36\20\2\u0086\u0083\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2"+
		"\u0088\u0089\7\61\2\2\u0089\u008a\7\21\2\2\u008a\u008b\5\f\7\2\u008b\u008c"+
		"\7<\2\2\u008c\u008d\7\23\2\2\u008d\13\3\2\2\2\u008e\u008f\5\16\b\2\u008f"+
		"\r\3\2\2\2\u0090\u0092\5\20\t\2\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2"+
		"\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\17\3\2\2\2\u0095\u0093"+
		"\3\2\2\2\u0096\u00a1\5\4\3\2\u0097\u00a1\5\"\22\2\u0098\u00a1\5 \21\2"+
		"\u0099\u00a1\5&\24\2\u009a\u00a1\5(\25\2\u009b\u00a1\5*\26\2\u009c\u00a1"+
		"\5,\27\2\u009d\u00a1\5.\30\2\u009e\u00a1\5\64\33\2\u009f\u00a1\5\60\31"+
		"\2\u00a0\u0096\3\2\2\2\u00a0\u0097\3\2\2\2\u00a0\u0098\3\2\2\2\u00a0\u0099"+
		"\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0\u009b\3\2\2\2\u00a0\u009c\3\2\2\2\u00a0"+
		"\u009d\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\21\3\2\2"+
		"\2\u00a2\u00a5\5\32\16\2\u00a3\u00a5\5\34\17\2\u00a4\u00a2\3\2\2\2\u00a4"+
		"\u00a3\3\2\2\2\u00a5\23\3\2\2\2\u00a6\u00a9\5\26\f\2\u00a7\u00a9\5\30"+
		"\r\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\25\3\2\2\2\u00aa\u00ab"+
		"\5\32\16\2\u00ab\u00ac\7.\2\2\u00ac\u00ad\5N(\2\u00ad\27\3\2\2\2\u00ae"+
		"\u00af\5\34\17\2\u00af\u00b0\7.\2\2\u00b0\u00b1\5N(\2\u00b1\31\3\2\2\2"+
		"\u00b2\u00b3\7\t\2\2\u00b3\33\3\2\2\2\u00b4\u00b8\7\t\2\2\u00b5\u00b6"+
		"\7\f\2\2\u00b6\u00b7\7\24\2\2\u00b7\u00b9\7\r\2\2\u00b8\u00b5\3\2\2\2"+
		"\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\35"+
		"\3\2\2\2\u00bc\u00bf\5\32\16\2\u00bd\u00bf\5\34\17\2\u00be\u00bc\3\2\2"+
		"\2\u00be\u00bd\3\2\2\2\u00bf\u00c7\3\2\2\2\u00c0\u00c3\7\22\2\2\u00c1"+
		"\u00c4\5\32\16\2\u00c2\u00c4\5\34\17\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2"+
		"\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7"+
		"\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\37\3\2\2\2\u00c9\u00c7\3\2\2"+
		"\2\u00ca\u00cb\7\64\2\2\u00cb\u00cc\58\35\2\u00cc\u00cd\7B\2\2\u00cd\u00d5"+
		"\5\16\b\2\u00ce\u00cf\7\67\2\2\u00cf\u00d0\58\35\2\u00d0\u00d1\7B\2\2"+
		"\u00d1\u00d2\5\16\b\2\u00d2\u00d4\3\2\2\2\u00d3\u00ce\3\2\2\2\u00d4\u00d7"+
		"\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00da\3\2\2\2\u00d7"+
		"\u00d5\3\2\2\2\u00d8\u00d9\7\62\2\2\u00d9\u00db\5\16\b\2\u00da\u00d8\3"+
		"\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\7A\2\2\u00dd"+
		"\u00de\7\23\2\2\u00de!\3\2\2\2\u00df\u00e2\5\32\16\2\u00e0\u00e2\5$\23"+
		"\2\u00e1\u00df\3\2\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4"+
		"\7.\2\2\u00e4\u00e5\58\35\2\u00e5\u00e6\7\20\2\2\u00e6#\3\2\2\2\u00e7"+
		"\u00e8\7\t\2\2\u00e8\u00e9\5\66\34\2\u00e9%\3\2\2\2\u00ea\u00eb\7=\2\2"+
		"\u00eb\u00ec\7\16\2\2\u00ec\u00ed\5\32\16\2\u00ed\u00ee\7.\2\2\u00ee\u00ef"+
		"\58\35\2\u00ef\u00f0\7\22\2\2\u00f0\u00f1\58\35\2\u00f1\u00f7\7\22\2\2"+
		"\u00f2\u00f3\5\32\16\2\u00f3\u00f4\7.\2\2\u00f4\u00f5\58\35\2\u00f5\u00f8"+
		"\3\2\2\2\u00f6\u00f8\5N(\2\u00f7\u00f2\3\2\2\2\u00f7\u00f6\3\2\2\2\u00f8"+
		"\u00f9\3\2\2\2\u00f9\u00fa\7\17\2\2\u00fa\u00fb\7@\2\2\u00fb\u00fc\5\16"+
		"\b\2\u00fc\u00fd\7\63\2\2\u00fd\u00fe\7\23\2\2\u00fe\'\3\2\2\2\u00ff\u0100"+
		"\7:\2\2\u0100\u0101\58\35\2\u0101\u0102\7@\2\2\u0102\u0103\5\16\b\2\u0103"+
		"\u0104\78\2\2\u0104\u0105\7\23\2\2\u0105)\3\2\2\2\u0106\u0107\7@\2\2\u0107"+
		"\u0108\5\16\b\2\u0108\u0109\7:\2\2\u0109\u010a\58\35\2\u010a\u010b\7\65"+
		"\2\2\u010b\u010c\7\23\2\2\u010c+\3\2\2\2\u010d\u010e\7\66\2\2\u010e\u010f"+
		"\7\20\2\2\u010f-\3\2\2\2\u0110\u0111\7;\2\2\u0111\u0112\7\20\2\2\u0112"+
		"/\3\2\2\2\u0113\u011c\7>\2\2\u0114\u0119\58\35\2\u0115\u0116\7\22\2\2"+
		"\u0116\u0118\58\35\2\u0117\u0115\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117"+
		"\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011c"+
		"\u0114\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\7\20"+
		"\2\2\u011f\61\3\2\2\2\u0120\u0121\7\t\2\2\u0121\u012a\7\16\2\2\u0122\u0127"+
		"\58\35\2\u0123\u0124\7\22\2\2\u0124\u0126\58\35\2\u0125\u0123\3\2\2\2"+
		"\u0126\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128\u012b"+
		"\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u0122\3\2\2\2\u012a\u012b\3\2\2\2\u012b"+
		"\u012c\3\2\2\2\u012c\u012d\7\17\2\2\u012d\63\3\2\2\2\u012e\u012f\5\62"+
		"\32\2\u012f\u0130\7\20\2\2\u0130\65\3\2\2\2\u0131\u0132\7\f\2\2\u0132"+
		"\u0133\58\35\2\u0133\u0134\7\r\2\2\u0134\u0136\3\2\2\2\u0135\u0131\3\2"+
		"\2\2\u0136\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138"+
		"\67\3\2\2\2\u0139\u013a\5:\36\2\u013a9\3\2\2\2\u013b\u013c\b\36\1\2\u013c"+
		"\u013d\5<\37\2\u013d\u0143\3\2\2\2\u013e\u013f\f\4\2\2\u013f\u0140\7\5"+
		"\2\2\u0140\u0142\5:\36\5\u0141\u013e\3\2\2\2\u0142\u0145\3\2\2\2\u0143"+
		"\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144;\3\2\2\2\u0145\u0143\3\2\2\2"+
		"\u0146\u0147\b\37\1\2\u0147\u0148\5> \2\u0148\u014e\3\2\2\2\u0149\u014a"+
		"\f\4\2\2\u014a\u014b\t\2\2\2\u014b\u014d\5> \2\u014c\u0149\3\2\2\2\u014d"+
		"\u0150\3\2\2\2\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f=\3\2\2\2"+
		"\u0150\u014e\3\2\2\2\u0151\u0152\b \1\2\u0152\u0153\5@!\2\u0153\u0159"+
		"\3\2\2\2\u0154\u0155\f\4\2\2\u0155\u0156\7\6\2\2\u0156\u0158\5@!\2\u0157"+
		"\u0154\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2"+
		"\2\2\u015a?\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\b!\1\2\u015d\u015e"+
		"\5B\"\2\u015e\u0164\3\2\2\2\u015f\u0160\f\4\2\2\u0160\u0161\7\7\2\2\u0161"+
		"\u0163\5B\"\2\u0162\u015f\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162\3\2"+
		"\2\2\u0164\u0165\3\2\2\2\u0165A\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168"+
		"\7+\2\2\u0168\u016b\5B\"\2\u0169\u016b\5D#\2\u016a\u0167\3\2\2\2\u016a"+
		"\u0169\3\2\2\2\u016bC\3\2\2\2\u016c\u016d\7\6\2\2\u016d\u0170\5D#\2\u016e"+
		"\u0170\5F$\2\u016f\u016c\3\2\2\2\u016f\u016e\3\2\2\2\u0170E\3\2\2\2\u0171"+
		"\u0172\b$\1\2\u0172\u0173\5H%\2\u0173\u0178\3\2\2\2\u0174\u0175\f\4\2"+
		"\2\u0175\u0177\5\66\34\2\u0176\u0174\3\2\2\2\u0177\u017a\3\2\2\2\u0178"+
		"\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179G\3\2\2\2\u017a\u0178\3\2\2\2"+
		"\u017b\u017e\5\62\32\2\u017c\u017e\5J&\2\u017d\u017b\3\2\2\2\u017d\u017c"+
		"\3\2\2\2\u017eI\3\2\2\2\u017f\u0180\7\16\2\2\u0180\u0181\58\35\2\u0181"+
		"\u0182\7\17\2\2\u0182\u0185\3\2\2\2\u0183\u0185\5L\'\2\u0184\u017f\3\2"+
		"\2\2\u0184\u0183\3\2\2\2\u0185K\3\2\2\2\u0186\u018a\7\t\2\2\u0187\u018a"+
		"\5N(\2\u0188\u018a\7\26\2\2\u0189\u0186\3\2\2\2\u0189\u0187\3\2\2\2\u0189"+
		"\u0188\3\2\2\2\u018aM\3\2\2\2\u018b\u0191\5X-\2\u018c\u0191\7\24\2\2\u018d"+
		"\u0191\7\25\2\2\u018e\u0191\7\26\2\2\u018f\u0191\7H\2\2\u0190\u018b\3"+
		"\2\2\2\u0190\u018c\3\2\2\2\u0190\u018d\3\2\2\2\u0190\u018e\3\2\2\2\u0190"+
		"\u018f\3\2\2\2\u0191O\3\2\2\2\u0192\u0197\7\24\2\2\u0193\u0194\7\22\2"+
		"\2\u0194\u0196\7\24\2\2\u0195\u0193\3\2\2\2\u0196\u0199\3\2\2\2\u0197"+
		"\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198Q\3\2\2\2\u0199\u0197\3\2\2\2"+
		"\u019a\u019f\7\25\2\2\u019b\u019c\7\22\2\2\u019c\u019e\7\25\2\2\u019d"+
		"\u019b\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2"+
		"\2\2\u01a0S\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a7\7H\2\2\u01a3\u01a4"+
		"\7\22\2\2\u01a4\u01a6\7H\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7"+
		"\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8U\3\2\2\2\u01a9\u01a7\3\2\2\2"+
		"\u01aa\u01ae\5P)\2\u01ab\u01ae\5R*\2\u01ac\u01ae\5T+\2\u01ad\u01aa\3\2"+
		"\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01aeW\3\2\2\2\u01af\u01be"+
		"\7\n\2\2\u01b0\u01b3\5X-\2\u01b1\u01b3\5V,\2\u01b2\u01b0\3\2\2\2\u01b2"+
		"\u01b1\3\2\2\2\u01b3\u01bb\3\2\2\2\u01b4\u01b7\7\22\2\2\u01b5\u01b8\5"+
		"X-\2\u01b6\u01b8\5V,\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01ba"+
		"\3\2\2\2\u01b9\u01b4\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb"+
		"\u01bc\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01b2\3\2"+
		"\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\7\13\2\2\u01c1"+
		"Y\3\2\2\2-]clrw{\u0086\u0093\u00a0\u00a4\u00a8\u00ba\u00be\u00c3\u00c7"+
		"\u00d5\u00da\u00e1\u00f7\u0119\u011c\u0127\u012a\u0137\u0143\u014e\u0159"+
		"\u0164\u016a\u016f\u0178\u017d\u0184\u0189\u0190\u0197\u019f\u01a7\u01ad"+
		"\u01b2\u01b7\u01bb\u01be";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}