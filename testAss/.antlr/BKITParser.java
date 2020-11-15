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
		RULE_non_initted_var = 8, RULE_var_init = 9, RULE_para_list = 10, RULE_if_stmt = 11, 
		RULE_assign_stmt = 12, RULE_for_stmt = 13, RULE_while_stmt = 14, RULE_do_while_stmt = 15, 
		RULE_break_stmt = 16, RULE_continue_stmt = 17, RULE_return_stmt = 18, 
		RULE_func_call = 19, RULE_call_stmt = 20, RULE_index_op = 21, RULE_expression = 22, 
		RULE_exp0 = 23, RULE_exp1 = 24, RULE_exp2 = 25, RULE_exp3 = 26, RULE_exp4 = 27, 
		RULE_exp5 = 28, RULE_exp6 = 29, RULE_exp7 = 30, RULE_exp8 = 31, RULE_operand = 32, 
		RULE_literals = 33, RULE_bool_array = 34, RULE_int_array = 35, RULE_float_array = 36, 
		RULE_string_array = 37, RULE_array_index = 38, RULE_array_list = 39;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "main_func", "func_declare", "func_body", 
			"stm_list", "stm", "non_initted_var", "var_init", "para_list", "if_stmt", 
			"assign_stmt", "for_stmt", "while_stmt", "do_while_stmt", "break_stmt", 
			"continue_stmt", "return_stmt", "func_call", "call_stmt", "index_op", 
			"expression", "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
			"exp7", "exp8", "operand", "literals", "bool_array", "int_array", "float_array", 
			"string_array", "array_index", "array_list"
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
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(80);
				var_declare();
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(86);
				func_declare();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(92);
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
		public Var_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare; }
	}

	public final Var_declareContext var_declare() throws RecognitionException {
		Var_declareContext _localctx = new Var_declareContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var_declare);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(VAR);
			setState(95);
			match(COLON);
			setState(96);
			var_list();
			setState(97);
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
		public List<Var_initContext> var_init() {
			return getRuleContexts(Var_initContext.class);
		}
		public Var_initContext var_init(int i) {
			return getRuleContext(Var_initContext.class,i);
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
			setState(101);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(99);
				var_init();
				}
				break;
			case 2:
				{
				setState(100);
				non_initted_var();
				}
				break;
			}
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(103);
				match(CM);
				setState(106);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
				case 1:
					{
					setState(104);
					var_init();
					}
					break;
				case 2:
					{
					setState(105);
					non_initted_var();
					}
					break;
				}
				}
				}
				setState(112);
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
			setState(115);
			match(FUNCTION);
			setState(116);
			match(COLON);
			setState(117);
			match(IDENTIFIER);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(118);
				match(PARAMETER);
				setState(119);
				match(COLON);
				setState(120);
				para_list();
				}
			}

			setState(123);
			match(BODY);
			setState(124);
			match(COLON);
			setState(125);
			func_body();
			setState(126);
			match(ENDBODY);
			setState(127);
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
	}

	public final Func_bodyContext func_body() throws RecognitionException {
		Func_bodyContext _localctx = new Func_bodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_func_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
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
		public List<Var_declareContext> var_declare() {
			return getRuleContexts(Var_declareContext.class);
		}
		public Var_declareContext var_declare(int i) {
			return getRuleContext(Var_declareContext.class,i);
		}
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
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(131);
				var_declare();
				}
				}
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(140);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(137);
					stm();
					}
					} 
				}
				setState(142);
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
			setState(152);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(143);
				assign_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(144);
				if_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(145);
				for_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(146);
				while_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(147);
				do_while_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(148);
				break_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(149);
				continue_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(150);
				call_stmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(151);
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
		public Non_initted_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_non_initted_var; }
	}

	public final Non_initted_varContext non_initted_var() throws RecognitionException {
		Non_initted_varContext _localctx = new Non_initted_varContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_non_initted_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			match(IDENTIFIER);
			setState(160);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LK) {
				{
				{
				setState(155);
				match(LK);
				setState(156);
				match(INTEGER);
				setState(157);
				match(RK);
				}
				}
				setState(162);
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

	public static class Var_initContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
		public LiteralsContext literals() {
			return getRuleContext(LiteralsContext.class,0);
		}
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
		public Var_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_init; }
	}

	public final Var_initContext var_init() throws RecognitionException {
		Var_initContext _localctx = new Var_initContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_var_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(IDENTIFIER);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LK) {
				{
				{
				setState(164);
				match(LK);
				setState(165);
				match(INTEGER);
				setState(166);
				match(RK);
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(172);
			match(AS);
			setState(173);
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

	public static class Para_listContext extends ParserRuleContext {
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
		public Para_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para_list; }
	}

	public final Para_listContext para_list() throws RecognitionException {
		Para_listContext _localctx = new Para_listContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_para_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			non_initted_var();
			setState(180);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(176);
				match(CM);
				setState(177);
				non_initted_var();
				}
				}
				setState(182);
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
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(IF);
			setState(184);
			expression();
			setState(185);
			match(THEN);
			setState(186);
			stm_list();
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(187);
				match(ELSEIF);
				setState(188);
				expression();
				setState(189);
				match(THEN);
				setState(190);
				stm_list();
				}
				}
				setState(196);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(197);
				match(ELSE);
				setState(198);
				stm_list();
				}
			}

			setState(201);
			match(ENDIF);
			setState(202);
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
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				{
				setState(204);
				match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(205);
				index_op();
				}
				break;
			}
			setState(208);
			match(AS);
			setState(209);
			expression();
			setState(210);
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

	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKITParser.FOR, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
		public TerminalNode AS() { return getToken(BKITParser.AS, 0); }
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
		public Exp1Context exp1() {
			return getRuleContext(Exp1Context.class,0);
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
		enterRule(_localctx, 26, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			match(FOR);
			setState(213);
			match(LP);
			setState(214);
			match(IDENTIFIER);
			setState(215);
			match(AS);
			setState(216);
			expression();
			setState(217);
			match(CM);
			setState(218);
			expression();
			setState(219);
			match(CM);
			setState(220);
			exp1(0);
			setState(221);
			match(RP);
			setState(222);
			match(DO);
			setState(223);
			stm_list();
			setState(224);
			match(ENDFOR);
			setState(225);
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
		enterRule(_localctx, 28, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			match(WHILE);
			setState(228);
			expression();
			setState(229);
			match(DO);
			setState(230);
			stm_list();
			setState(231);
			match(ENDWHILE);
			setState(232);
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
		enterRule(_localctx, 30, RULE_do_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(DO);
			setState(235);
			stm_list();
			setState(236);
			match(WHILE);
			setState(237);
			expression();
			setState(238);
			match(ENDDO);
			setState(239);
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
		enterRule(_localctx, 32, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(BREAK);
			setState(242);
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
		enterRule(_localctx, 34, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			match(CONTINUE);
			setState(245);
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
		enterRule(_localctx, 36, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(RETURN);
			setState(256);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDSUB) | (1L << IDENTIFIER) | (1L << LB) | (1L << LP) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOLEAN) | (1L << BNEG))) != 0) || _la==LSTRING) {
				{
				setState(248);
				expression();
				setState(253);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(249);
					match(CM);
					setState(250);
					expression();
					}
					}
					setState(255);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(258);
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
		enterRule(_localctx, 38, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(IDENTIFIER);
			setState(261);
			match(LP);
			setState(270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ADDSUB) | (1L << IDENTIFIER) | (1L << LB) | (1L << LP) | (1L << INTEGER) | (1L << FLOAT) | (1L << BOLEAN) | (1L << BNEG))) != 0) || _la==LSTRING) {
				{
				setState(262);
				expression();
				setState(267);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(263);
					match(CM);
					setState(264);
					expression();
					}
					}
					setState(269);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(272);
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
		enterRule(_localctx, 40, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(274);
			func_call();
			setState(275);
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
		public Exp7Context exp7() {
			return getRuleContext(Exp7Context.class,0);
		}
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
		enterRule(_localctx, 42, RULE_index_op);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			exp7();
			setState(282); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(278);
					match(LK);
					setState(279);
					expression();
					setState(280);
					match(RK);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(284); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
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
		enterRule(_localctx, 44, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(286);
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
		enterRule(_localctx, 46, RULE_exp0);
		try {
			setState(293);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(288);
				exp1(0);
				setState(289);
				match(RELATION_OP);
				setState(290);
				exp1(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(292);
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
		int _startState = 48;
		enterRecursionRule(_localctx, 48, RULE_exp1, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(296);
			exp2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(303);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp1);
					setState(298);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(299);
					_la = _input.LA(1);
					if ( !(_la==BAND || _la==BOR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(300);
					exp2(0);
					}
					} 
				}
				setState(305);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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
		int _startState = 50;
		enterRecursionRule(_localctx, 50, RULE_exp2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(307);
			exp3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(314);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp2);
					setState(309);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(310);
					match(ADDSUB);
					}
					setState(311);
					exp3(0);
					}
					} 
				}
				setState(316);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
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
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_exp3, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(318);
			exp4();
			}
			_ctx.stop = _input.LT(-1);
			setState(325);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Exp3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_exp3);
					setState(320);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					{
					setState(321);
					match(MULDIV);
					}
					setState(322);
					exp4();
					}
					} 
				}
				setState(327);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
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
		enterRule(_localctx, 54, RULE_exp4);
		try {
			setState(331);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BNEG:
				enterOuterAlt(_localctx, 1);
				{
				setState(328);
				match(BNEG);
				setState(329);
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
				setState(330);
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
		enterRule(_localctx, 56, RULE_exp5);
		try {
			setState(336);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADDSUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(333);
				match(ADDSUB);
				setState(334);
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
				setState(335);
				exp6();
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
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
		}
		public Exp7Context exp7() {
			return getRuleContext(Exp7Context.class,0);
		}
		public Exp6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp6; }
	}

	public final Exp6Context exp6() throws RecognitionException {
		Exp6Context _localctx = new Exp6Context(_ctx, getState());
		enterRule(_localctx, 58, RULE_exp6);
		try {
			setState(340);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				index_op();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(339);
				exp7();
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
		enterRule(_localctx, 60, RULE_exp7);
		try {
			setState(344);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(342);
				func_call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(343);
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
		enterRule(_localctx, 62, RULE_exp8);
		try {
			setState(351);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LP:
				enterOuterAlt(_localctx, 1);
				{
				setState(346);
				match(LP);
				{
				setState(347);
				expression();
				}
				setState(348);
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
				setState(350);
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
		enterRule(_localctx, 64, RULE_operand);
		try {
			setState(355);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(353);
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
				setState(354);
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
		enterRule(_localctx, 66, RULE_literals);
		try {
			setState(362);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				setState(357);
				array_list();
				}
				break;
			case INTEGER:
				enterOuterAlt(_localctx, 2);
				{
				setState(358);
				match(INTEGER);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(359);
				match(FLOAT);
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 4);
				{
				setState(360);
				match(BOLEAN);
				}
				break;
			case LSTRING:
				enterOuterAlt(_localctx, 5);
				{
				setState(361);
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

	public static class Bool_arrayContext extends ParserRuleContext {
		public List<TerminalNode> BOLEAN() { return getTokens(BKITParser.BOLEAN); }
		public TerminalNode BOLEAN(int i) {
			return getToken(BKITParser.BOLEAN, i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public Bool_arrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool_array; }
	}

	public final Bool_arrayContext bool_array() throws RecognitionException {
		Bool_arrayContext _localctx = new Bool_arrayContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_bool_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			match(BOLEAN);
			setState(369);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(365);
					match(CM);
					setState(366);
					match(BOLEAN);
					}
					} 
				}
				setState(371);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
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
		enterRule(_localctx, 70, RULE_int_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(372);
			match(INTEGER);
			setState(377);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(373);
					match(CM);
					setState(374);
					match(INTEGER);
					}
					} 
				}
				setState(379);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
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
		enterRule(_localctx, 72, RULE_float_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			match(FLOAT);
			setState(385);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(381);
					match(CM);
					setState(382);
					match(FLOAT);
					}
					} 
				}
				setState(387);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
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
		enterRule(_localctx, 74, RULE_string_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(388);
			match(LSTRING);
			setState(393);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,34,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(389);
					match(CM);
					setState(390);
					match(LSTRING);
					}
					} 
				}
				setState(395);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,34,_ctx);
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
		public Bool_arrayContext bool_array() {
			return getRuleContext(Bool_arrayContext.class,0);
		}
		public Array_indexContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_index; }
	}

	public final Array_indexContext array_index() throws RecognitionException {
		Array_indexContext _localctx = new Array_indexContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_array_index);
		try {
			setState(400);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER:
				enterOuterAlt(_localctx, 1);
				{
				setState(396);
				int_array();
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				setState(397);
				float_array();
				}
				break;
			case LSTRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(398);
				string_array();
				}
				break;
			case BOLEAN:
				enterOuterAlt(_localctx, 4);
				{
				setState(399);
				bool_array();
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
	}

	public final Array_listContext array_list() throws RecognitionException {
		Array_listContext _localctx = new Array_listContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_array_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			match(LB);
			setState(417);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 8)) & ~0x3f) == 0 && ((1L << (_la - 8)) & ((1L << (LB - 8)) | (1L << (INTEGER - 8)) | (1L << (FLOAT - 8)) | (1L << (BOLEAN - 8)) | (1L << (LSTRING - 8)))) != 0)) {
				{
				setState(405);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LB:
					{
					setState(403);
					array_list();
					}
					break;
				case INTEGER:
				case FLOAT:
				case BOLEAN:
				case LSTRING:
					{
					setState(404);
					array_index();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(414);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(407);
					match(CM);
					setState(410);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case LB:
						{
						setState(408);
						array_list();
						}
						break;
					case INTEGER:
					case FLOAT:
					case BOLEAN:
					case LSTRING:
						{
						setState(409);
						array_index();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					}
					setState(416);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(419);
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
		case 24:
			return exp1_sempred((Exp1Context)_localctx, predIndex);
		case 25:
			return exp2_sempred((Exp2Context)_localctx, predIndex);
		case 26:
			return exp3_sempred((Exp3Context)_localctx, predIndex);
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H\u01a8\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\7\2T\n\2\f"+
		"\2\16\2W\13\2\3\2\7\2Z\n\2\f\2\16\2]\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3"+
		"\3\4\3\4\5\4h\n\4\3\4\3\4\3\4\5\4m\n\4\7\4o\n\4\f\4\16\4r\13\4\3\5\3\5"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\5\6|\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b"+
		"\7\b\u0087\n\b\f\b\16\b\u008a\13\b\3\b\7\b\u008d\n\b\f\b\16\b\u0090\13"+
		"\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u009b\n\t\3\n\3\n\3\n\3\n\7"+
		"\n\u00a1\n\n\f\n\16\n\u00a4\13\n\3\13\3\13\3\13\3\13\7\13\u00aa\n\13\f"+
		"\13\16\13\u00ad\13\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u00b5\n\f\f\f\16"+
		"\f\u00b8\13\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00c3\n\r\f\r\16"+
		"\r\u00c6\13\r\3\r\3\r\5\r\u00ca\n\r\3\r\3\r\3\r\3\16\3\16\5\16\u00d1\n"+
		"\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3"+
		"\24\3\24\7\24\u00fe\n\24\f\24\16\24\u0101\13\24\5\24\u0103\n\24\3\24\3"+
		"\24\3\25\3\25\3\25\3\25\3\25\7\25\u010c\n\25\f\25\16\25\u010f\13\25\5"+
		"\25\u0111\n\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\6\27"+
		"\u011d\n\27\r\27\16\27\u011e\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0128"+
		"\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0130\n\32\f\32\16\32\u0133\13"+
		"\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u013b\n\33\f\33\16\33\u013e\13"+
		"\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0146\n\34\f\34\16\34\u0149\13"+
		"\34\3\35\3\35\3\35\5\35\u014e\n\35\3\36\3\36\3\36\5\36\u0153\n\36\3\37"+
		"\3\37\5\37\u0157\n\37\3 \3 \5 \u015b\n \3!\3!\3!\3!\3!\5!\u0162\n!\3\""+
		"\3\"\5\"\u0166\n\"\3#\3#\3#\3#\3#\5#\u016d\n#\3$\3$\3$\7$\u0172\n$\f$"+
		"\16$\u0175\13$\3%\3%\3%\7%\u017a\n%\f%\16%\u017d\13%\3&\3&\3&\7&\u0182"+
		"\n&\f&\16&\u0185\13&\3\'\3\'\3\'\7\'\u018a\n\'\f\'\16\'\u018d\13\'\3("+
		"\3(\3(\3(\5(\u0193\n(\3)\3)\3)\5)\u0198\n)\3)\3)\3)\5)\u019d\n)\7)\u019f"+
		"\n)\f)\16)\u01a2\13)\5)\u01a4\n)\3)\3)\3)\2\5\62\64\66*\2\4\6\b\n\f\16"+
		"\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP\2\3\3\2,-\2"+
		"\u01b3\2U\3\2\2\2\4`\3\2\2\2\6g\3\2\2\2\bs\3\2\2\2\nu\3\2\2\2\f\u0083"+
		"\3\2\2\2\16\u0088\3\2\2\2\20\u009a\3\2\2\2\22\u009c\3\2\2\2\24\u00a5\3"+
		"\2\2\2\26\u00b1\3\2\2\2\30\u00b9\3\2\2\2\32\u00d0\3\2\2\2\34\u00d6\3\2"+
		"\2\2\36\u00e5\3\2\2\2 \u00ec\3\2\2\2\"\u00f3\3\2\2\2$\u00f6\3\2\2\2&\u00f9"+
		"\3\2\2\2(\u0106\3\2\2\2*\u0114\3\2\2\2,\u0117\3\2\2\2.\u0120\3\2\2\2\60"+
		"\u0127\3\2\2\2\62\u0129\3\2\2\2\64\u0134\3\2\2\2\66\u013f\3\2\2\28\u014d"+
		"\3\2\2\2:\u0152\3\2\2\2<\u0156\3\2\2\2>\u015a\3\2\2\2@\u0161\3\2\2\2B"+
		"\u0165\3\2\2\2D\u016c\3\2\2\2F\u016e\3\2\2\2H\u0176\3\2\2\2J\u017e\3\2"+
		"\2\2L\u0186\3\2\2\2N\u0192\3\2\2\2P\u0194\3\2\2\2RT\5\4\3\2SR\3\2\2\2"+
		"TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V[\3\2\2\2WU\3\2\2\2XZ\5\n\6\2YX\3\2\2\2"+
		"Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2][\3\2\2\2^_\7\2\2\3_\3\3\2"+
		"\2\2`a\7/\2\2ab\7\21\2\2bc\5\6\4\2cd\7\20\2\2d\5\3\2\2\2eh\5\24\13\2f"+
		"h\5\22\n\2ge\3\2\2\2gf\3\2\2\2hp\3\2\2\2il\7\22\2\2jm\5\24\13\2km\5\22"+
		"\n\2lj\3\2\2\2lk\3\2\2\2mo\3\2\2\2ni\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2"+
		"\2\2q\7\3\2\2\2rp\3\2\2\2st\3\2\2\2t\t\3\2\2\2uv\7\60\2\2vw\7\21\2\2w"+
		"{\7\t\2\2xy\79\2\2yz\7\21\2\2z|\5\26\f\2{x\3\2\2\2{|\3\2\2\2|}\3\2\2\2"+
		"}~\7\61\2\2~\177\7\21\2\2\177\u0080\5\f\7\2\u0080\u0081\7<\2\2\u0081\u0082"+
		"\7\23\2\2\u0082\13\3\2\2\2\u0083\u0084\5\16\b\2\u0084\r\3\2\2\2\u0085"+
		"\u0087\5\4\3\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2"+
		"\2\2\u0088\u0089\3\2\2\2\u0089\u008e\3\2\2\2\u008a\u0088\3\2\2\2\u008b"+
		"\u008d\5\20\t\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3"+
		"\2\2\2\u008e\u008f\3\2\2\2\u008f\17\3\2\2\2\u0090\u008e\3\2\2\2\u0091"+
		"\u009b\5\32\16\2\u0092\u009b\5\30\r\2\u0093\u009b\5\34\17\2\u0094\u009b"+
		"\5\36\20\2\u0095\u009b\5 \21\2\u0096\u009b\5\"\22\2\u0097\u009b\5$\23"+
		"\2\u0098\u009b\5*\26\2\u0099\u009b\5&\24\2\u009a\u0091\3\2\2\2\u009a\u0092"+
		"\3\2\2\2\u009a\u0093\3\2\2\2\u009a\u0094\3\2\2\2\u009a\u0095\3\2\2\2\u009a"+
		"\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2"+
		"\2\2\u009b\21\3\2\2\2\u009c\u00a2\7\t\2\2\u009d\u009e\7\f\2\2\u009e\u009f"+
		"\7\24\2\2\u009f\u00a1\7\r\2\2\u00a0\u009d\3\2\2\2\u00a1\u00a4\3\2\2\2"+
		"\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\23\3\2\2\2\u00a4\u00a2"+
		"\3\2\2\2\u00a5\u00ab\7\t\2\2\u00a6\u00a7\7\f\2\2\u00a7\u00a8\7\24\2\2"+
		"\u00a8\u00aa\7\r\2\2\u00a9\u00a6\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9"+
		"\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae"+
		"\u00af\7.\2\2\u00af\u00b0\5D#\2\u00b0\25\3\2\2\2\u00b1\u00b6\5\22\n\2"+
		"\u00b2\u00b3\7\22\2\2\u00b3\u00b5\5\22\n\2\u00b4\u00b2\3\2\2\2\u00b5\u00b8"+
		"\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\27\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b9\u00ba\7\64\2\2\u00ba\u00bb\5.\30\2\u00bb\u00bc\7"+
		"B\2\2\u00bc\u00c4\5\16\b\2\u00bd\u00be\7\67\2\2\u00be\u00bf\5.\30\2\u00bf"+
		"\u00c0\7B\2\2\u00c0\u00c1\5\16\b\2\u00c1\u00c3\3\2\2\2\u00c2\u00bd\3\2"+
		"\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5"+
		"\u00c9\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7\62\2\2\u00c8\u00ca\5"+
		"\16\b\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb"+
		"\u00cc\7A\2\2\u00cc\u00cd\7\23\2\2\u00cd\31\3\2\2\2\u00ce\u00d1\7\t\2"+
		"\2\u00cf\u00d1\5,\27\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2"+
		"\3\2\2\2\u00d2\u00d3\7.\2\2\u00d3\u00d4\5.\30\2\u00d4\u00d5\7\20\2\2\u00d5"+
		"\33\3\2\2\2\u00d6\u00d7\7=\2\2\u00d7\u00d8\7\16\2\2\u00d8\u00d9\7\t\2"+
		"\2\u00d9\u00da\7.\2\2\u00da\u00db\5.\30\2\u00db\u00dc\7\22\2\2\u00dc\u00dd"+
		"\5.\30\2\u00dd\u00de\7\22\2\2\u00de\u00df\5\62\32\2\u00df\u00e0\7\17\2"+
		"\2\u00e0\u00e1\7@\2\2\u00e1\u00e2\5\16\b\2\u00e2\u00e3\7\63\2\2\u00e3"+
		"\u00e4\7\23\2\2\u00e4\35\3\2\2\2\u00e5\u00e6\7:\2\2\u00e6\u00e7\5.\30"+
		"\2\u00e7\u00e8\7@\2\2\u00e8\u00e9\5\16\b\2\u00e9\u00ea\78\2\2\u00ea\u00eb"+
		"\7\23\2\2\u00eb\37\3\2\2\2\u00ec\u00ed\7@\2\2\u00ed\u00ee\5\16\b\2\u00ee"+
		"\u00ef\7:\2\2\u00ef\u00f0\5.\30\2\u00f0\u00f1\7\65\2\2\u00f1\u00f2\7\23"+
		"\2\2\u00f2!\3\2\2\2\u00f3\u00f4\7\66\2\2\u00f4\u00f5\7\20\2\2\u00f5#\3"+
		"\2\2\2\u00f6\u00f7\7;\2\2\u00f7\u00f8\7\20\2\2\u00f8%\3\2\2\2\u00f9\u0102"+
		"\7>\2\2\u00fa\u00ff\5.\30\2\u00fb\u00fc\7\22\2\2\u00fc\u00fe\5.\30\2\u00fd"+
		"\u00fb\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2"+
		"\2\2\u0100\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0102\u00fa\3\2\2\2\u0102"+
		"\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\7\20\2\2\u0105\'\3\2\2"+
		"\2\u0106\u0107\7\t\2\2\u0107\u0110\7\16\2\2\u0108\u010d\5.\30\2\u0109"+
		"\u010a\7\22\2\2\u010a\u010c\5.\30\2\u010b\u0109\3\2\2\2\u010c\u010f\3"+
		"\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0111\3\2\2\2\u010f"+
		"\u010d\3\2\2\2\u0110\u0108\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2"+
		"\2\2\u0112\u0113\7\17\2\2\u0113)\3\2\2\2\u0114\u0115\5(\25\2\u0115\u0116"+
		"\7\20\2\2\u0116+\3\2\2\2\u0117\u011c\5> \2\u0118\u0119\7\f\2\2\u0119\u011a"+
		"\5.\30\2\u011a\u011b\7\r\2\2\u011b\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011d"+
		"\u011e\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f-\3\2\2\2"+
		"\u0120\u0121\5\60\31\2\u0121/\3\2\2\2\u0122\u0123\5\62\32\2\u0123\u0124"+
		"\7\5\2\2\u0124\u0125\5\62\32\2\u0125\u0128\3\2\2\2\u0126\u0128\5\62\32"+
		"\2\u0127\u0122\3\2\2\2\u0127\u0126\3\2\2\2\u0128\61\3\2\2\2\u0129\u012a"+
		"\b\32\1\2\u012a\u012b\5\64\33\2\u012b\u0131\3\2\2\2\u012c\u012d\f\4\2"+
		"\2\u012d\u012e\t\2\2\2\u012e\u0130\5\64\33\2\u012f\u012c\3\2\2\2\u0130"+
		"\u0133\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132\63\3\2\2"+
		"\2\u0133\u0131\3\2\2\2\u0134\u0135\b\33\1\2\u0135\u0136\5\66\34\2\u0136"+
		"\u013c\3\2\2\2\u0137\u0138\f\4\2\2\u0138\u0139\7\6\2\2\u0139\u013b\5\66"+
		"\34\2\u013a\u0137\3\2\2\2\u013b\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c"+
		"\u013d\3\2\2\2\u013d\65\3\2\2\2\u013e\u013c\3\2\2\2\u013f\u0140\b\34\1"+
		"\2\u0140\u0141\58\35\2\u0141\u0147\3\2\2\2\u0142\u0143\f\4\2\2\u0143\u0144"+
		"\7\7\2\2\u0144\u0146\58\35\2\u0145\u0142\3\2\2\2\u0146\u0149\3\2\2\2\u0147"+
		"\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148\67\3\2\2\2\u0149\u0147\3\2\2"+
		"\2\u014a\u014b\7+\2\2\u014b\u014e\58\35\2\u014c\u014e\5:\36\2\u014d\u014a"+
		"\3\2\2\2\u014d\u014c\3\2\2\2\u014e9\3\2\2\2\u014f\u0150\7\6\2\2\u0150"+
		"\u0153\5:\36\2\u0151\u0153\5<\37\2\u0152\u014f\3\2\2\2\u0152\u0151\3\2"+
		"\2\2\u0153;\3\2\2\2\u0154\u0157\5,\27\2\u0155\u0157\5> \2\u0156\u0154"+
		"\3\2\2\2\u0156\u0155\3\2\2\2\u0157=\3\2\2\2\u0158\u015b\5(\25\2\u0159"+
		"\u015b\5@!\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015b?\3\2\2\2\u015c"+
		"\u015d\7\16\2\2\u015d\u015e\5.\30\2\u015e\u015f\7\17\2\2\u015f\u0162\3"+
		"\2\2\2\u0160\u0162\5B\"\2\u0161\u015c\3\2\2\2\u0161\u0160\3\2\2\2\u0162"+
		"A\3\2\2\2\u0163\u0166\7\t\2\2\u0164\u0166\5D#\2\u0165\u0163\3\2\2\2\u0165"+
		"\u0164\3\2\2\2\u0166C\3\2\2\2\u0167\u016d\5P)\2\u0168\u016d\7\24\2\2\u0169"+
		"\u016d\7\25\2\2\u016a\u016d\7\26\2\2\u016b\u016d\7H\2\2\u016c\u0167\3"+
		"\2\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c"+
		"\u016b\3\2\2\2\u016dE\3\2\2\2\u016e\u0173\7\26\2\2\u016f\u0170\7\22\2"+
		"\2\u0170\u0172\7\26\2\2\u0171\u016f\3\2\2\2\u0172\u0175\3\2\2\2\u0173"+
		"\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174G\3\2\2\2\u0175\u0173\3\2\2\2"+
		"\u0176\u017b\7\24\2\2\u0177\u0178\7\22\2\2\u0178\u017a\7\24\2\2\u0179"+
		"\u0177\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017c\3\2"+
		"\2\2\u017cI\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0183\7\25\2\2\u017f\u0180"+
		"\7\22\2\2\u0180\u0182\7\25\2\2\u0181\u017f\3\2\2\2\u0182\u0185\3\2\2\2"+
		"\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184K\3\2\2\2\u0185\u0183\3"+
		"\2\2\2\u0186\u018b\7H\2\2\u0187\u0188\7\22\2\2\u0188\u018a\7H\2\2\u0189"+
		"\u0187\3\2\2\2\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2"+
		"\2\2\u018cM\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0193\5H%\2\u018f\u0193"+
		"\5J&\2\u0190\u0193\5L\'\2\u0191\u0193\5F$\2\u0192\u018e\3\2\2\2\u0192"+
		"\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2\u0193O\3\2\2\2"+
		"\u0194\u01a3\7\n\2\2\u0195\u0198\5P)\2\u0196\u0198\5N(\2\u0197\u0195\3"+
		"\2\2\2\u0197\u0196\3\2\2\2\u0198\u01a0\3\2\2\2\u0199\u019c\7\22\2\2\u019a"+
		"\u019d\5P)\2\u019b\u019d\5N(\2\u019c\u019a\3\2\2\2\u019c\u019b\3\2\2\2"+
		"\u019d\u019f\3\2\2\2\u019e\u0199\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e"+
		"\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3"+
		"\u0197\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\7\13"+
		"\2\2\u01a6Q\3\2\2\2*U[glp{\u0088\u008e\u009a\u00a2\u00ab\u00b6\u00c4\u00c9"+
		"\u00d0\u00ff\u0102\u010d\u0110\u011e\u0127\u0131\u013c\u0147\u014d\u0152"+
		"\u0156\u015a\u0161\u0165\u016c\u0173\u017b\u0183\u018b\u0192\u0197\u019c"+
		"\u01a0\u01a3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}