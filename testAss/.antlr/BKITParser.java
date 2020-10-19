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
		RULE_para_list = 8, RULE_non_initted_var = 9, RULE_initted_var = 10, RULE_scalar_init = 11, 
		RULE_composite_init = 12, RULE_scalar_var = 13, RULE_composite_var = 14, 
		RULE_if_stmt = 15, RULE_assign_stmt = 16, RULE_composite_ass = 17, RULE_for_stmt = 18, 
		RULE_while_stmt = 19, RULE_do_while_stmt = 20, RULE_break_stmt = 21, RULE_continue_stmt = 22, 
		RULE_return_stmt = 23, RULE_func_call = 24, RULE_call_stmt = 25, RULE_index_op = 26, 
		RULE_expression = 27, RULE_exp0 = 28, RULE_exp1 = 29, RULE_exp2 = 30, 
		RULE_exp3 = 31, RULE_exp4 = 32, RULE_exp5 = 33, RULE_exp6 = 34, RULE_exp7 = 35, 
		RULE_exp8 = 36, RULE_operand = 37, RULE_literals = 38, RULE_int_array = 39, 
		RULE_float_array = 40, RULE_string_array = 41, RULE_array_index = 42, 
		RULE_array_list = 43;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "main_func", "func_declare", "func_body", 
			"stm_list", "stm", "para_list", "non_initted_var", "initted_var", "scalar_init", 
			"composite_init", "scalar_var", "composite_var", "if_stmt", "assign_stmt", 
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
		public List<Var_declareContext> var_declare() {
			return getRuleContexts(Var_declareContext.class);
		}
		public Var_declareContext var_declare(int i) {
			return getRuleContext(Var_declareContext.class,i);
		}
		public Func_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_body; }
	}

	public final Func_bodyContext func_body() throws RecognitionException {
		Func_bodyContext _localctx = new Func_bodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_func_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(140);
				var_declare();
				}
				}
				setState(145);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(146);
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
		enterRule(_localctx, 12, RULE_stm_list);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(148);
					stm();
					}
					} 
				}
				setState(153);
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

	public static class StmContext extends ParserRuleContext {
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
	}

	public final StmContext stm() throws RecognitionException {
		StmContext _localctx = new StmContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_stm);
		try {
			setState(163);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(154);
				assign_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(155);
				if_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(156);
				for_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(157);
				while_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(158);
				do_while_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(159);
				break_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(160);
				continue_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(161);
				call_stmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(162);
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
	}

	public final Para_listContext para_list() throws RecognitionException {
		Para_listContext _localctx = new Para_listContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_para_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(165);
				scalar_var();
				}
				break;
			case 2:
				{
				setState(166);
				composite_var();
				}
				break;
			}
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(169);
				match(CM);
				setState(172);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
				case 1:
					{
					setState(170);
					scalar_var();
					}
					break;
				case 2:
					{
					setState(171);
					composite_var();
					}
					break;
				}
				}
				}
				setState(178);
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
		enterRule(_localctx, 18, RULE_non_initted_var);
		try {
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(179);
				scalar_var();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(180);
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
		enterRule(_localctx, 20, RULE_initted_var);
		try {
			setState(185);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				scalar_init();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(184);
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
		enterRule(_localctx, 22, RULE_scalar_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			scalar_var();
			setState(188);
			match(AS);
			setState(189);
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
		enterRule(_localctx, 24, RULE_composite_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			composite_var();
			setState(192);
			match(AS);
			setState(193);
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
		enterRule(_localctx, 26, RULE_scalar_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
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
		enterRule(_localctx, 28, RULE_composite_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(IDENTIFIER);
			setState(201); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(198);
				match(LK);
				setState(199);
				match(INTEGER);
				setState(200);
				match(RK);
				}
				}
				setState(203); 
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
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205);
			match(IF);
			setState(206);
			expression();
			setState(207);
			match(THEN);
			setState(208);
			stm_list();
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(209);
				match(ELSEIF);
				setState(210);
				expression();
				setState(211);
				match(THEN);
				setState(212);
				stm_list();
				}
				}
				setState(218);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(221);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(219);
				match(ELSE);
				setState(220);
				stm_list();
				}
			}

			setState(223);
			match(ENDIF);
			setState(224);
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
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(226);
				scalar_var();
				}
				break;
			case 2:
				{
				setState(227);
				composite_ass();
				}
				break;
			}
			setState(230);
			match(AS);
			setState(231);
			expression();
			setState(232);
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
	}

	public final Composite_assContext composite_ass() throws RecognitionException {
		Composite_assContext _localctx = new Composite_assContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_composite_ass);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(IDENTIFIER);
			setState(235);
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
		public Scalar_initContext scalar_init() {
			return getRuleContext(Scalar_initContext.class,0);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stm_listContext stm_list() {
			return getRuleContext(Stm_listContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(BKITParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public For_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stmt; }
	}

	public final For_stmtContext for_stmt() throws RecognitionException {
		For_stmtContext _localctx = new For_stmtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(FOR);
			setState(238);
			match(LP);
			setState(239);
			scalar_init();
			setState(240);
			match(CM);
			setState(241);
			expression();
			setState(242);
			match(CM);
			setState(243);
			expression();
			setState(244);
			match(RP);
			setState(245);
			match(DO);
			setState(246);
			stm_list();
			setState(247);
			match(ENDFOR);
			setState(248);
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
	}

	public final While_stmtContext while_stmt() throws RecognitionException {
		While_stmtContext _localctx = new While_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(WHILE);
			setState(251);
			expression();
			setState(252);
			match(DO);
			setState(253);
			stm_list();
			setState(254);
			match(ENDWHILE);
			setState(255);
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
	}

	public final Do_while_stmtContext do_while_stmt() throws RecognitionException {
		Do_while_stmtContext _localctx = new Do_while_stmtContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_do_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(DO);
			setState(258);
			stm_list();
			setState(259);
			match(WHILE);
			setState(260);
			expression();
			setState(261);
			match(ENDDO);
			setState(262);
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
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			match(BREAK);
			setState(265);
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
	}

	public final Continue_stmtContext continue_stmt() throws RecognitionException {
		Continue_stmtContext _localctx = new Continue_stmtContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(CONTINUE);
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
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(270);
			match(RETURN);
			setState(279);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDSUB) | (1L << IDENTIFIER) | (1L << LB) | (1L << LP) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOLEAN) | (1L << BNEG))) != 0) || _la==LSTRING) {
				{
				setState(271);
				expression();
				setState(276);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(272);
					match(CM);
					setState(273);
					expression();
					}
					}
					setState(278);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(281);
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
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			match(IDENTIFIER);
			setState(284);
			match(LP);
			setState(293);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDSUB) | (1L << IDENTIFIER) | (1L << LB) | (1L << LP) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOLEAN) | (1L << BNEG))) != 0) || _la==LSTRING) {
				{
				setState(285);
				expression();
				setState(290);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(286);
					match(CM);
					setState(287);
					expression();
					}
					}
					setState(292);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(295);
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
	}

	public final Call_stmtContext call_stmt() throws RecognitionException {
		Call_stmtContext _localctx = new Call_stmtContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			func_call();
			setState(298);
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
	}

	public final Index_opContext index_op() throws RecognitionException {
		Index_opContext _localctx = new Index_opContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_index_op);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(304); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(300);
					match(LK);
					setState(301);
					expression();
					setState(302);
					match(RK);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(306); 
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
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			exp0();
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
		public List<Exp1Context> exp1() {
			return getRuleContexts(Exp1Context.class);
		}
		public Exp1Context exp1(int i) {
			return getRuleContext(Exp1Context.class,i);
		}
		public TerminalNode RELATION_OP() { return getToken(BKITParser.RELATION_OP, 0); }
		public Exp0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp0; }
	}

	public final Exp0Context exp0() throws RecognitionException {
		Exp0Context _localctx = new Exp0Context(_ctx, getState());
		enterRule(_localctx, 56, RULE_exp0);
		try {
			setState(315);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(310);
				exp1(0);
				setState(311);
				match(RELATION_OP);
				setState(312);
				exp1(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(314);
				exp1(0);
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
			setState(318);
			exp2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(325);
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
					setState(320);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(321);
					_la = _input.LA(1);
					if ( !(_la==BAND || _la==BOR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(322);
					exp2(0);
					}
					} 
				}
				setState(327);
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
			setState(329);
			exp3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(336);
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
					setState(331);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(332);
					match(ADDSUB);
					}
					setState(333);
					exp3(0);
					}
					} 
				}
				setState(338);
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
			setState(340);
			exp4();
			}
			_ctx.stop = _input.LT(-1);
			setState(347);
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
					setState(342);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(343);
					match(MULDIV);
					}
					setState(344);
					exp4();
					}
					} 
				}
				setState(349);
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
	}

	public final Exp4Context exp4() throws RecognitionException {
		Exp4Context _localctx = new Exp4Context(_ctx, getState());
		enterRule(_localctx, 64, RULE_exp4);
		try {
			setState(353);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BNEG:
				enterOuterAlt(_localctx, 1);
				{
				setState(350);
				match(BNEG);
				setState(351);
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
				setState(352);
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
	}

	public final Exp5Context exp5() throws RecognitionException {
		Exp5Context _localctx = new Exp5Context(_ctx, getState());
		enterRule(_localctx, 66, RULE_exp5);
		try {
			setState(358);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADDSUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(355);
				match(ADDSUB);
				setState(356);
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
				setState(357);
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
			setState(361);
			exp7();
			}
			_ctx.stop = _input.LT(-1);
			setState(367);
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
					setState(363);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(364);
					index_op();
					}
					} 
				}
				setState(369);
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
	}

	public final Exp7Context exp7() throws RecognitionException {
		Exp7Context _localctx = new Exp7Context(_ctx, getState());
		enterRule(_localctx, 70, RULE_exp7);
		try {
			setState(372);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(370);
				func_call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(371);
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
	}

	public final Exp8Context exp8() throws RecognitionException {
		Exp8Context _localctx = new Exp8Context(_ctx, getState());
		enterRule(_localctx, 72, RULE_exp8);
		try {
			setState(379);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(374);
				match(LP);
				{
				setState(375);
				expression();
				}
				setState(376);
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
				setState(378);
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
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_operand);
		try {
			setState(383);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(381);
				match(IDENTIFIER);
				}
				break;
			case LB:
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case LSTRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(382);
				literals();
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
	}

	public final LiteralsContext literals() throws RecognitionException {
		LiteralsContext _localctx = new LiteralsContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_literals);
		try {
			setState(390);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				setState(385);
				array_list();
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(386);
				match(INTEGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(387);
				match(FLOAT);
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 4);
				{
				setState(388);
				match(BOLEAN);
				}
				break;
			case LSTRING:
				enterOuterAlt(_localctx, 5);
				{
				setState(389);
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
	}

	public final Int_arrayContext int_array() throws RecognitionException {
		Int_arrayContext _localctx = new Int_arrayContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_int_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(392);
			match(INTEGER);
			setState(397);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(393);
					match(CM);
					setState(394);
					match(INTEGER);
					}
					} 
				}
				setState(399);
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
	}

	public final Float_arrayContext float_array() throws RecognitionException {
		Float_arrayContext _localctx = new Float_arrayContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_float_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(400);
			match(FLOAT);
			setState(405);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(401);
					match(CM);
					setState(402);
					match(FLOAT);
					}
					} 
				}
				setState(407);
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
	}

	public final String_arrayContext string_array() throws RecognitionException {
		String_arrayContext _localctx = new String_arrayContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_string_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(408);
			match(LSTRING);
			setState(413);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,37,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(409);
					match(CM);
					setState(410);
					match(LSTRING);
					}
					} 
				}
				setState(415);
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
	}

	public final Array_indexContext array_index() throws RecognitionException {
		Array_indexContext _localctx = new Array_indexContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_array_index);
		try {
			setState(419);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(416);
				int_array();
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(417);
				float_array();
				}
				break;
			case LSTRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(418);
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
		public List<Array_indexContext> array_index() {
			return getRuleContexts(Array_indexContext.class);
		}
		public Array_indexContext array_index(int i) {
			return getRuleContext(Array_indexContext.class,i);
		}
		public List<Array_listContext> array_list() {
			return getRuleContexts(Array_listContext.class);
		}
		public Array_listContext array_list(int i) {
			return getRuleContext(Array_listContext.class,i);
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
		enterRule(_localctx, 86, RULE_array_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(421);
			match(LB);
			setState(436);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & ((1L << (LB - 8)) | (1L << (INTEGER - 8)) | (1L << (FLOAT - 8)) | (1L << (LSTRING - 8)))) != 0)) {
				{
				setState(424);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INTEGER:
				case FLOAT:
				case LSTRING:
					{
					setState(422);
					array_index();
					}
					break;
				case LB:
					{
					setState(423);
					array_list();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(433);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(426);
					match(CM);
					setState(429);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case INTEGER:
					case FLOAT:
					case LSTRING:
						{
						setState(427);
						array_index();
						}
						break;
					case LB:
						{
						setState(428);
						array_list();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					}
					setState(435);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(438);
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
	private boolean exp1_sempred(Exp1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp2_sempred(Exp2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp3_sempred(Exp3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp6_sempred(Exp6Context _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H\u01bb\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\3\2\7\2\\\n\2\f\2\16\2_\13\2\3\2\7\2b\n\2\f\2\16\2e\13\2\3"+
		"\2\3\2\3\3\3\3\3\3\3\3\5\3m\n\3\3\3\3\3\3\4\3\4\5\4s\n\4\3\4\3\4\3\4\5"+
		"\4x\n\4\7\4z\n\4\f\4\16\4}\13\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0087"+
		"\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\7\7\u0090\n\7\f\7\16\7\u0093\13\7\3\7"+
		"\3\7\3\b\7\b\u0098\n\b\f\b\16\b\u009b\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\5\t\u00a6\n\t\3\n\3\n\5\n\u00aa\n\n\3\n\3\n\3\n\5\n\u00af\n\n"+
		"\7\n\u00b1\n\n\f\n\16\n\u00b4\13\n\3\13\3\13\5\13\u00b8\n\13\3\f\3\f\5"+
		"\f\u00bc\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3"+
		"\20\3\20\6\20\u00cc\n\20\r\20\16\20\u00cd\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\7\21\u00d9\n\21\f\21\16\21\u00dc\13\21\3\21\3\21\5\21"+
		"\u00e0\n\21\3\21\3\21\3\21\3\22\3\22\5\22\u00e7\n\22\3\22\3\22\3\22\3"+
		"\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3"+
		"\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3"+
		"\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u0115"+
		"\n\31\f\31\16\31\u0118\13\31\5\31\u011a\n\31\3\31\3\31\3\32\3\32\3\32"+
		"\3\32\3\32\7\32\u0123\n\32\f\32\16\32\u0126\13\32\5\32\u0128\n\32\3\32"+
		"\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\6\34\u0133\n\34\r\34\16\34\u0134"+
		"\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u013e\n\36\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\7\37\u0146\n\37\f\37\16\37\u0149\13\37\3 \3 \3 \3 \3 \3 \7"+
		" \u0151\n \f \16 \u0154\13 \3!\3!\3!\3!\3!\3!\7!\u015c\n!\f!\16!\u015f"+
		"\13!\3\"\3\"\3\"\5\"\u0164\n\"\3#\3#\3#\5#\u0169\n#\3$\3$\3$\3$\3$\7$"+
		"\u0170\n$\f$\16$\u0173\13$\3%\3%\5%\u0177\n%\3&\3&\3&\3&\3&\5&\u017e\n"+
		"&\3\'\3\'\5\'\u0182\n\'\3(\3(\3(\3(\3(\5(\u0189\n(\3)\3)\3)\7)\u018e\n"+
		")\f)\16)\u0191\13)\3*\3*\3*\7*\u0196\n*\f*\16*\u0199\13*\3+\3+\3+\7+\u019e"+
		"\n+\f+\16+\u01a1\13+\3,\3,\3,\5,\u01a6\n,\3-\3-\3-\5-\u01ab\n-\3-\3-\3"+
		"-\5-\u01b0\n-\7-\u01b2\n-\f-\16-\u01b5\13-\5-\u01b7\n-\3-\3-\3-\2\6<>"+
		"@F.\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B"+
		"DFHJLNPRTVX\2\3\3\2,-\2\u01c4\2]\3\2\2\2\4h\3\2\2\2\6r\3\2\2\2\b~\3\2"+
		"\2\2\n\u0080\3\2\2\2\f\u0091\3\2\2\2\16\u0099\3\2\2\2\20\u00a5\3\2\2\2"+
		"\22\u00a9\3\2\2\2\24\u00b7\3\2\2\2\26\u00bb\3\2\2\2\30\u00bd\3\2\2\2\32"+
		"\u00c1\3\2\2\2\34\u00c5\3\2\2\2\36\u00c7\3\2\2\2 \u00cf\3\2\2\2\"\u00e6"+
		"\3\2\2\2$\u00ec\3\2\2\2&\u00ef\3\2\2\2(\u00fc\3\2\2\2*\u0103\3\2\2\2,"+
		"\u010a\3\2\2\2.\u010d\3\2\2\2\60\u0110\3\2\2\2\62\u011d\3\2\2\2\64\u012b"+
		"\3\2\2\2\66\u0132\3\2\2\28\u0136\3\2\2\2:\u013d\3\2\2\2<\u013f\3\2\2\2"+
		">\u014a\3\2\2\2@\u0155\3\2\2\2B\u0163\3\2\2\2D\u0168\3\2\2\2F\u016a\3"+
		"\2\2\2H\u0176\3\2\2\2J\u017d\3\2\2\2L\u0181\3\2\2\2N\u0188\3\2\2\2P\u018a"+
		"\3\2\2\2R\u0192\3\2\2\2T\u019a\3\2\2\2V\u01a5\3\2\2\2X\u01a7\3\2\2\2Z"+
		"\\\5\4\3\2[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^c\3\2\2\2_]\3\2\2"+
		"\2`b\5\n\6\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2\2\2df\3\2\2\2ec\3\2\2"+
		"\2fg\7\2\2\3g\3\3\2\2\2hi\7/\2\2ij\7\21\2\2jl\5\6\4\2km\7.\2\2lk\3\2\2"+
		"\2lm\3\2\2\2mn\3\2\2\2no\7\20\2\2o\5\3\2\2\2ps\5\26\f\2qs\5\24\13\2rp"+
		"\3\2\2\2rq\3\2\2\2s{\3\2\2\2tw\7\22\2\2ux\5\26\f\2vx\5\24\13\2wu\3\2\2"+
		"\2wv\3\2\2\2xz\3\2\2\2yt\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\7\3\2"+
		"\2\2}{\3\2\2\2~\177\3\2\2\2\177\t\3\2\2\2\u0080\u0081\7\60\2\2\u0081\u0082"+
		"\7\21\2\2\u0082\u0086\7\t\2\2\u0083\u0084\79\2\2\u0084\u0085\7\21\2\2"+
		"\u0085\u0087\5\22\n\2\u0086\u0083\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088"+
		"\3\2\2\2\u0088\u0089\7\61\2\2\u0089\u008a\7\21\2\2\u008a\u008b\5\f\7\2"+
		"\u008b\u008c\7<\2\2\u008c\u008d\7\23\2\2\u008d\13\3\2\2\2\u008e\u0090"+
		"\5\4\3\2\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091"+
		"\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\5\16"+
		"\b\2\u0095\r\3\2\2\2\u0096\u0098\5\20\t\2\u0097\u0096\3\2\2\2\u0098\u009b"+
		"\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\17\3\2\2\2\u009b"+
		"\u0099\3\2\2\2\u009c\u00a6\5\"\22\2\u009d\u00a6\5 \21\2\u009e\u00a6\5"+
		"&\24\2\u009f\u00a6\5(\25\2\u00a0\u00a6\5*\26\2\u00a1\u00a6\5,\27\2\u00a2"+
		"\u00a6\5.\30\2\u00a3\u00a6\5\64\33\2\u00a4\u00a6\5\60\31\2\u00a5\u009c"+
		"\3\2\2\2\u00a5\u009d\3\2\2\2\u00a5\u009e\3\2\2\2\u00a5\u009f\3\2\2\2\u00a5"+
		"\u00a0\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2"+
		"\2\2\u00a5\u00a4\3\2\2\2\u00a6\21\3\2\2\2\u00a7\u00aa\5\34\17\2\u00a8"+
		"\u00aa\5\36\20\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00b2\3"+
		"\2\2\2\u00ab\u00ae\7\22\2\2\u00ac\u00af\5\34\17\2\u00ad\u00af\5\36\20"+
		"\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ab"+
		"\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3"+
		"\23\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b8\5\34\17\2\u00b6\u00b8\5\36"+
		"\20\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\25\3\2\2\2\u00b9\u00bc"+
		"\5\30\r\2\u00ba\u00bc\5\32\16\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2"+
		"\2\u00bc\27\3\2\2\2\u00bd\u00be\5\34\17\2\u00be\u00bf\7.\2\2\u00bf\u00c0"+
		"\5N(\2\u00c0\31\3\2\2\2\u00c1\u00c2\5\36\20\2\u00c2\u00c3\7.\2\2\u00c3"+
		"\u00c4\5N(\2\u00c4\33\3\2\2\2\u00c5\u00c6\7\t\2\2\u00c6\35\3\2\2\2\u00c7"+
		"\u00cb\7\t\2\2\u00c8\u00c9\7\f\2\2\u00c9\u00ca\7\24\2\2\u00ca\u00cc\7"+
		"\r\2\2\u00cb\u00c8\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd"+
		"\u00ce\3\2\2\2\u00ce\37\3\2\2\2\u00cf\u00d0\7\64\2\2\u00d0\u00d1\58\35"+
		"\2\u00d1\u00d2\7B\2\2\u00d2\u00da\5\16\b\2\u00d3\u00d4\7\67\2\2\u00d4"+
		"\u00d5\58\35\2\u00d5\u00d6\7B\2\2\u00d6\u00d7\5\16\b\2\u00d7\u00d9\3\2"+
		"\2\2\u00d8\u00d3\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2\u00da"+
		"\u00db\3\2\2\2\u00db\u00df\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\7\62"+
		"\2\2\u00de\u00e0\5\16\b\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0"+
		"\u00e1\3\2\2\2\u00e1\u00e2\7A\2\2\u00e2\u00e3\7\23\2\2\u00e3!\3\2\2\2"+
		"\u00e4\u00e7\5\34\17\2\u00e5\u00e7\5$\23\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5"+
		"\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\7.\2\2\u00e9\u00ea\58\35\2\u00ea"+
		"\u00eb\7\20\2\2\u00eb#\3\2\2\2\u00ec\u00ed\7\t\2\2\u00ed\u00ee\5\66\34"+
		"\2\u00ee%\3\2\2\2\u00ef\u00f0\7=\2\2\u00f0\u00f1\7\16\2\2\u00f1\u00f2"+
		"\5\30\r\2\u00f2\u00f3\7\22\2\2\u00f3\u00f4\58\35\2\u00f4\u00f5\7\22\2"+
		"\2\u00f5\u00f6\58\35\2\u00f6\u00f7\7\17\2\2\u00f7\u00f8\7@\2\2\u00f8\u00f9"+
		"\5\16\b\2\u00f9\u00fa\7\63\2\2\u00fa\u00fb\7\23\2\2\u00fb\'\3\2\2\2\u00fc"+
		"\u00fd\7:\2\2\u00fd\u00fe\58\35\2\u00fe\u00ff\7@\2\2\u00ff\u0100\5\16"+
		"\b\2\u0100\u0101\78\2\2\u0101\u0102\7\23\2\2\u0102)\3\2\2\2\u0103\u0104"+
		"\7@\2\2\u0104\u0105\5\16\b\2\u0105\u0106\7:\2\2\u0106\u0107\58\35\2\u0107"+
		"\u0108\7\65\2\2\u0108\u0109\7\23\2\2\u0109+\3\2\2\2\u010a\u010b\7\66\2"+
		"\2\u010b\u010c\7\20\2\2\u010c-\3\2\2\2\u010d\u010e\7;\2\2\u010e\u010f"+
		"\7\20\2\2\u010f/\3\2\2\2\u0110\u0119\7>\2\2\u0111\u0116\58\35\2\u0112"+
		"\u0113\7\22\2\2\u0113\u0115\58\35\2\u0114\u0112\3\2\2\2\u0115\u0118\3"+
		"\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u011a\3\2\2\2\u0118"+
		"\u0116\3\2\2\2\u0119\u0111\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\3\2"+
		"\2\2\u011b\u011c\7\20\2\2\u011c\61\3\2\2\2\u011d\u011e\7\t\2\2\u011e\u0127"+
		"\7\16\2\2\u011f\u0124\58\35\2\u0120\u0121\7\22\2\2\u0121\u0123\58\35\2"+
		"\u0122\u0120\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125"+
		"\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0127\u011f\3\2\2\2\u0127"+
		"\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\7\17\2\2\u012a\63\3\2\2"+
		"\2\u012b\u012c\5\62\32\2\u012c\u012d\7\20\2\2\u012d\65\3\2\2\2\u012e\u012f"+
		"\7\f\2\2\u012f\u0130\58\35\2\u0130\u0131\7\r\2\2\u0131\u0133\3\2\2\2\u0132"+
		"\u012e\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2"+
		"\2\2\u0135\67\3\2\2\2\u0136\u0137\5:\36\2\u01379\3\2\2\2\u0138\u0139\5"+
		"<\37\2\u0139\u013a\7\5\2\2\u013a\u013b\5<\37\2\u013b\u013e\3\2\2\2\u013c"+
		"\u013e\5<\37\2\u013d\u0138\3\2\2\2\u013d\u013c\3\2\2\2\u013e;\3\2\2\2"+
		"\u013f\u0140\b\37\1\2\u0140\u0141\5> \2\u0141\u0147\3\2\2\2\u0142\u0143"+
		"\f\4\2\2\u0143\u0144\t\2\2\2\u0144\u0146\5> \2\u0145\u0142\3\2\2\2\u0146"+
		"\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148=\3\2\2\2"+
		"\u0149\u0147\3\2\2\2\u014a\u014b\b \1\2\u014b\u014c\5@!\2\u014c\u0152"+
		"\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\7\6\2\2\u014f\u0151\5@!\2\u0150"+
		"\u014d\3\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2"+
		"\2\2\u0153?\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\b!\1\2\u0156\u0157"+
		"\5B\"\2\u0157\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159\u015a\7\7\2\2\u015a"+
		"\u015c\5B\"\2\u015b\u0158\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2"+
		"\2\2\u015d\u015e\3\2\2\2\u015eA\3\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161"+
		"\7+\2\2\u0161\u0164\5B\"\2\u0162\u0164\5D#\2\u0163\u0160\3\2\2\2\u0163"+
		"\u0162\3\2\2\2\u0164C\3\2\2\2\u0165\u0166\7\6\2\2\u0166\u0169\5D#\2\u0167"+
		"\u0169\5F$\2\u0168\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169E\3\2\2\2\u016a"+
		"\u016b\b$\1\2\u016b\u016c\5H%\2\u016c\u0171\3\2\2\2\u016d\u016e\f\4\2"+
		"\2\u016e\u0170\5\66\34\2\u016f\u016d\3\2\2\2\u0170\u0173\3\2\2\2\u0171"+
		"\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172G\3\2\2\2\u0173\u0171\3\2\2\2"+
		"\u0174\u0177\5\62\32\2\u0175\u0177\5J&\2\u0176\u0174\3\2\2\2\u0176\u0175"+
		"\3\2\2\2\u0177I\3\2\2\2\u0178\u0179\7\16\2\2\u0179\u017a\58\35\2\u017a"+
		"\u017b\7\17\2\2\u017b\u017e\3\2\2\2\u017c\u017e\5L\'\2\u017d\u0178\3\2"+
		"\2\2\u017d\u017c\3\2\2\2\u017eK\3\2\2\2\u017f\u0182\7\t\2\2\u0180\u0182"+
		"\5N(\2\u0181\u017f\3\2\2\2\u0181\u0180\3\2\2\2\u0182M\3\2\2\2\u0183\u0189"+
		"\5X-\2\u0184\u0189\7\24\2\2\u0185\u0189\7\25\2\2\u0186\u0189\7\26\2\2"+
		"\u0187\u0189\7H\2\2\u0188\u0183\3\2\2\2\u0188\u0184\3\2\2\2\u0188\u0185"+
		"\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0187\3\2\2\2\u0189O\3\2\2\2\u018a"+
		"\u018f\7\24\2\2\u018b\u018c\7\22\2\2\u018c\u018e\7\24\2\2\u018d\u018b"+
		"\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190"+
		"Q\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0197\7\25\2\2\u0193\u0194\7\22\2"+
		"\2\u0194\u0196\7\25\2\2\u0195\u0193\3\2\2\2\u0196\u0199\3\2\2\2\u0197"+
		"\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198S\3\2\2\2\u0199\u0197\3\2\2\2"+
		"\u019a\u019f\7H\2\2\u019b\u019c\7\22\2\2\u019c\u019e\7H\2\2\u019d\u019b"+
		"\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0"+
		"U\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a6\5P)\2\u01a3\u01a6\5R*\2\u01a4"+
		"\u01a6\5T+\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2"+
		"\2\u01a6W\3\2\2\2\u01a7\u01b6\7\n\2\2\u01a8\u01ab\5V,\2\u01a9\u01ab\5"+
		"X-\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01b3\3\2\2\2\u01ac"+
		"\u01af\7\22\2\2\u01ad\u01b0\5V,\2\u01ae\u01b0\5X-\2\u01af\u01ad\3\2\2"+
		"\2\u01af\u01ae\3\2\2\2\u01b0\u01b2\3\2\2\2\u01b1\u01ac\3\2\2\2\u01b2\u01b5"+
		"\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5"+
		"\u01b3\3\2\2\2\u01b6\u01aa\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2"+
		"\2\2\u01b8\u01b9\7\13\2\2\u01b9Y\3\2\2\2-]clrw{\u0086\u0091\u0099\u00a5"+
		"\u00a9\u00ae\u00b2\u00b7\u00bb\u00cd\u00da\u00df\u00e6\u0116\u0119\u0124"+
		"\u0127\u0134\u013d\u0147\u0152\u015d\u0163\u0168\u0171\u0176\u017d\u0181"+
		"\u0188\u018f\u0197\u019f\u01a5\u01aa\u01af\u01b3\u01b6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}