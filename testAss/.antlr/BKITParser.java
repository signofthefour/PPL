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
		WS=1, COMMENT=2, RELATION_OP=3, MULDIV=4, IDENTIFIER=5, LB=6, RB=7, LK=8, 
		RK=9, LP=10, RP=11, SEMI=12, COLON=13, CM=14, DOT=15, INTEGER=16, FLOAT=17, 
		BOLEAN=18, FADDOP=19, IADDOP=20, FSUBOP=21, ISUBOP=22, FMULOP=23, IMULOP=24, 
		FDIVOP=25, IDIVOP=26, IREMAIN=27, EQUAL=28, FNEQUAL=29, FLESSOE=30, FGROE=31, 
		FLESS=32, FGR=33, INEQUAL=34, ILESSOE=35, IGROE=36, ILESS=37, IGR=38, 
		BNEG=39, BAND=40, BOR=41, AS=42, VAR=43, FUNCTION=44, BODY=45, ELSE=46, 
		ENDFOR=47, IF=48, ENDDO=49, BREAK=50, ELSEIF=51, ENDWHILE=52, PARAMETER=53, 
		WHILE=54, CONTINUE=55, ENDBODY=56, FOR=57, RETURN=58, TRUE=59, DO=60, 
		ENDIF=61, THEN=62, FALSE=63, ERROR_CHAR=64, UNCLOSE_STRING=65, ILLEGAL_ESCAPE=66, 
		UNTERMINATED_COMMENT=67, LSTRING=68;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_var_list = 2, RULE_decl = 3, 
		RULE_main_func = 4, RULE_func_declare = 5, RULE_func_body = 6, RULE_stm_list = 7, 
		RULE_stm = 8, RULE_non_initted_var = 9, RULE_var_init = 10, RULE_para_list = 11, 
		RULE_if_stmt = 12, RULE_assign_stmt = 13, RULE_for_stmt = 14, RULE_while_stmt = 15, 
		RULE_do_while_stmt = 16, RULE_break_stmt = 17, RULE_continue_stmt = 18, 
		RULE_return_stmt = 19, RULE_func_call = 20, RULE_call_stmt = 21, RULE_index_op = 22, 
		RULE_expression = 23, RULE_exp0 = 24, RULE_exp1 = 25, RULE_exp2 = 26, 
		RULE_exp3 = 27, RULE_exp4 = 28, RULE_exp5 = 29, RULE_exp6 = 30, RULE_exp7 = 31, 
		RULE_exp8 = 32, RULE_operand = 33, RULE_literals = 34, RULE_bool_array = 35, 
		RULE_int_array = 36, RULE_float_array = 37, RULE_string_array = 38, RULE_array_index = 39, 
		RULE_array_list = 40, RULE_element = 41, RULE_arraylit = 42;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "var_list", "decl", "main_func", "func_declare", 
			"func_body", "stm_list", "stm", "non_initted_var", "var_init", "para_list", 
			"if_stmt", "assign_stmt", "for_stmt", "while_stmt", "do_while_stmt", 
			"break_stmt", "continue_stmt", "return_stmt", "func_call", "call_stmt", 
			"index_op", "expression", "exp0", "exp1", "exp2", "exp3", "exp4", "exp5", 
			"exp6", "exp7", "exp8", "operand", "literals", "bool_array", "int_array", 
			"float_array", "string_array", "array_index", "array_list", "element", 
			"arraylit"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, "'{'", "'}'", "'['", "']'", "'('", 
			"')'", "';'", "':'", "','", "'.'", null, null, null, "'+.'", "'+'", "'-.'", 
			"'-'", "'*.'", "'*'", "'\\.'", "'\\'", "'%'", "'=='", "'=/='", "'<=.'", 
			"'>=.'", "'<.'", "'>.'", "'!='", "'<='", "'>='", "'<'", "'>'", "'!'", 
			"'&&'", "'||'", "'='", "'Var'", "'Function'", "'Body'", "'Else'", "'EndFor'", 
			"'If'", "'EndDo'", "'Break'", "'ElseIf'", "'EndWhile'", "'Parameter'", 
			"'While'", "'Continue'", "'EndBody'", "'For'", "'Return'", "'True'", 
			"'Do'", "'EndIf'", "'Then'", "'False'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "WS", "COMMENT", "RELATION_OP", "MULDIV", "IDENTIFIER", "LB", "RB", 
			"LK", "RK", "LP", "RP", "SEMI", "COLON", "CM", "DOT", "INTEGER", "FLOAT", 
			"BOLEAN", "FADDOP", "IADDOP", "FSUBOP", "ISUBOP", "FMULOP", "IMULOP", 
			"FDIVOP", "IDIVOP", "IREMAIN", "EQUAL", "FNEQUAL", "FLESSOE", "FGROE", 
			"FLESS", "FGR", "INEQUAL", "ILESSOE", "IGROE", "ILESS", "IGR", "BNEG", 
			"BAND", "BOR", "AS", "VAR", "FUNCTION", "BODY", "ELSE", "ENDFOR", "IF", 
			"ENDDO", "BREAK", "ELSEIF", "ENDWHILE", "PARAMETER", "WHILE", "CONTINUE", 
			"ENDBODY", "FOR", "RETURN", "TRUE", "DO", "ENDIF", "THEN", "FALSE", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "LSTRING"
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
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(86);
				var_declare();
				}
				}
				setState(91);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(92);
				func_declare();
				}
				}
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(98);
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
			setState(100);
			match(VAR);
			setState(101);
			match(COLON);
			setState(102);
			var_list();
			setState(103);
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
		public List<DeclContext> decl() {
			return getRuleContexts(DeclContext.class);
		}
		public DeclContext decl(int i) {
			return getRuleContext(DeclContext.class,i);
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
			setState(105);
			decl();
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(106);
				match(CM);
				setState(107);
				decl();
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

	public static class DeclContext extends ParserRuleContext {
		public Var_initContext var_init() {
			return getRuleContext(Var_initContext.class,0);
		}
		public Non_initted_varContext non_initted_var() {
			return getRuleContext(Non_initted_varContext.class,0);
		}
		public DeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decl; }
	}

	public final DeclContext decl() throws RecognitionException {
		DeclContext _localctx = new DeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_decl);
		try {
			setState(115);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				var_init();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(114);
				non_initted_var();
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

	public static class Main_funcContext extends ParserRuleContext {
		public Main_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_func; }
	}

	public final Main_funcContext main_func() throws RecognitionException {
		Main_funcContext _localctx = new Main_funcContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_main_func);
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
		enterRule(_localctx, 10, RULE_func_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(FUNCTION);
			setState(120);
			match(COLON);
			setState(121);
			match(IDENTIFIER);
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(122);
				match(PARAMETER);
				setState(123);
				match(COLON);
				setState(124);
				para_list();
				}
			}

			setState(127);
			match(BODY);
			setState(128);
			match(COLON);
			setState(129);
			func_body();
			setState(130);
			match(ENDBODY);
			setState(131);
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
		enterRule(_localctx, 12, RULE_func_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
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
		enterRule(_localctx, 14, RULE_stm_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(135);
				var_declare();
				}
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(144);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(141);
					stm();
					}
					} 
				}
				setState(146);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
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
		enterRule(_localctx, 16, RULE_stm);
		try {
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(147);
				assign_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				if_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(149);
				for_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(150);
				while_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(151);
				do_while_stmt();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(152);
				break_stmt();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(153);
				continue_stmt();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(154);
				call_stmt();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(155);
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
		enterRule(_localctx, 18, RULE_non_initted_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(IDENTIFIER);
			setState(164);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LK) {
				{
				{
				setState(159);
				match(LK);
				setState(160);
				match(INTEGER);
				setState(161);
				match(RK);
				}
				}
				setState(166);
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
		enterRule(_localctx, 20, RULE_var_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(167);
			match(IDENTIFIER);
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LK) {
				{
				{
				setState(168);
				match(LK);
				setState(169);
				match(INTEGER);
				setState(170);
				match(RK);
				}
				}
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(176);
			match(AS);
			setState(177);
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
		enterRule(_localctx, 22, RULE_para_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
			non_initted_var();
			setState(184);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(180);
				match(CM);
				setState(181);
				non_initted_var();
				}
				}
				setState(186);
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
		enterRule(_localctx, 24, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(IF);
			setState(188);
			expression();
			setState(189);
			match(THEN);
			setState(190);
			stm_list();
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(191);
				match(ELSEIF);
				setState(192);
				expression();
				setState(193);
				match(THEN);
				setState(194);
				stm_list();
				}
				}
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(201);
				match(ELSE);
				setState(202);
				stm_list();
				}
			}

			setState(205);
			match(ENDIF);
			setState(206);
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
		enterRule(_localctx, 26, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				setState(208);
				match(IDENTIFIER);
				}
				break;
			case 2:
				{
				setState(209);
				index_op();
				}
				break;
			}
			setState(212);
			match(AS);
			setState(213);
			expression();
			setState(214);
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
		enterRule(_localctx, 28, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			match(FOR);
			setState(217);
			match(LP);
			setState(218);
			match(IDENTIFIER);
			setState(219);
			match(AS);
			setState(220);
			expression();
			setState(221);
			match(CM);
			setState(222);
			expression();
			setState(223);
			match(CM);
			setState(224);
			exp1(0);
			setState(225);
			match(RP);
			setState(226);
			match(DO);
			setState(227);
			stm_list();
			setState(228);
			match(ENDFOR);
			setState(229);
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
		enterRule(_localctx, 30, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(WHILE);
			setState(232);
			expression();
			setState(233);
			match(DO);
			setState(234);
			stm_list();
			setState(235);
			match(ENDWHILE);
			setState(236);
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
		enterRule(_localctx, 32, RULE_do_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(DO);
			setState(239);
			stm_list();
			setState(240);
			match(WHILE);
			setState(241);
			expression();
			setState(242);
			match(ENDDO);
			setState(243);
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
		enterRule(_localctx, 34, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(BREAK);
			setState(246);
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
		enterRule(_localctx, 36, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(CONTINUE);
			setState(249);
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
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Return_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stmt; }
	}

	public final Return_stmtContext return_stmt() throws RecognitionException {
		Return_stmtContext _localctx = new Return_stmtContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			match(RETURN);
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 5)) & ~0x3f) == 0 && ((1L << (_la - 5)) & ((1L << (IDENTIFIER - 5)) | (1L << (LB - 5)) | (1L << (LP - 5)) | (1L << (INTEGER - 5)) | (1L << (FLOAT - 5)) | (1L << (BOLEAN - 5)) | (1L << (FSUBOP - 5)) | (1L << (ISUBOP - 5)) | (1L << (BNEG - 5)) | (1L << (LSTRING - 5)))) != 0)) {
				{
				setState(252);
				expression();
				}
			}

			setState(255);
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
		enterRule(_localctx, 40, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(IDENTIFIER);
			setState(258);
			match(LP);
			setState(267);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 5)) & ~0x3f) == 0 && ((1L << (_la - 5)) & ((1L << (IDENTIFIER - 5)) | (1L << (LB - 5)) | (1L << (LP - 5)) | (1L << (INTEGER - 5)) | (1L << (FLOAT - 5)) | (1L << (BOLEAN - 5)) | (1L << (FSUBOP - 5)) | (1L << (ISUBOP - 5)) | (1L << (BNEG - 5)) | (1L << (LSTRING - 5)))) != 0)) {
				{
				setState(259);
				expression();
				setState(264);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(260);
					match(CM);
					setState(261);
					expression();
					}
					}
					setState(266);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(269);
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
		enterRule(_localctx, 42, RULE_call_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			func_call();
			setState(272);
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
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode IDENTIFIER() { return getToken(BKITParser.IDENTIFIER, 0); }
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
		enterRule(_localctx, 44, RULE_index_op);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				setState(274);
				func_call();
				}
				break;
			case 2:
				{
				setState(275);
				match(IDENTIFIER);
				}
				break;
			}
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
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
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
		enterRule(_localctx, 46, RULE_expression);
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
		enterRule(_localctx, 48, RULE_exp0);
		try {
			setState(293);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
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
		int _startState = 50;
		enterRecursionRule(_localctx, 50, RULE_exp1, _p);
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
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
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
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
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
		public TerminalNode FADDOP() { return getToken(BKITParser.FADDOP, 0); }
		public TerminalNode FSUBOP() { return getToken(BKITParser.FSUBOP, 0); }
		public TerminalNode IADDOP() { return getToken(BKITParser.IADDOP, 0); }
		public TerminalNode ISUBOP() { return getToken(BKITParser.ISUBOP, 0); }
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
		int _startState = 52;
		enterRecursionRule(_localctx, 52, RULE_exp2, _p);
		int _la;
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
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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
					setState(310);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << FADDOP) | (1L << IADDOP) | (1L << FSUBOP) | (1L << ISUBOP))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(311);
					exp3(0);
					}
					} 
				}
				setState(316);
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
		int _startState = 54;
		enterRecursionRule(_localctx, 54, RULE_exp3, _p);
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
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
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
					setState(321);
					match(MULDIV);
					setState(322);
					exp4();
					}
					} 
				}
				setState(327);
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
		enterRule(_localctx, 56, RULE_exp4);
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
			case IDENTIFIER:
			case LB:
			case LP:
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case FSUBOP:
			case ISUBOP:
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
		public Exp5Context exp5() {
			return getRuleContext(Exp5Context.class,0);
		}
		public TerminalNode FSUBOP() { return getToken(BKITParser.FSUBOP, 0); }
		public TerminalNode ISUBOP() { return getToken(BKITParser.ISUBOP, 0); }
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
		enterRule(_localctx, 58, RULE_exp5);
		int _la;
		try {
			setState(336);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FSUBOP:
			case ISUBOP:
				enterOuterAlt(_localctx, 1);
				{
				setState(333);
				_la = _input.LA(1);
				if ( !(_la==FSUBOP || _la==ISUBOP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
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
		enterRule(_localctx, 60, RULE_exp6);
		try {
			setState(340);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
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
		enterRule(_localctx, 62, RULE_exp7);
		try {
			setState(344);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
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
		enterRule(_localctx, 64, RULE_exp8);
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
		enterRule(_localctx, 66, RULE_operand);
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
		public ArraylitContext arraylit() {
			return getRuleContext(ArraylitContext.class,0);
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
		enterRule(_localctx, 68, RULE_literals);
		try {
			setState(362);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				setState(357);
				arraylit();
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
		enterRule(_localctx, 70, RULE_bool_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			match(BOLEAN);
			setState(369);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
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
		enterRule(_localctx, 72, RULE_int_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(372);
			match(INTEGER);
			setState(377);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
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
		enterRule(_localctx, 74, RULE_float_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(380);
			match(FLOAT);
			setState(385);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,32,_ctx);
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
		enterRule(_localctx, 76, RULE_string_array);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(388);
			match(LSTRING);
			setState(393);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,33,_ctx);
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
		enterRule(_localctx, 78, RULE_array_index);
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
		public List<ElementContext> element() {
			return getRuleContexts(ElementContext.class);
		}
		public ElementContext element(int i) {
			return getRuleContext(ElementContext.class,i);
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
		enterRule(_localctx, 80, RULE_array_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			match(LB);
			setState(411);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 6)) & ~0x3f) == 0 && ((1L << (_la - 6)) & ((1L << (LB - 6)) | (1L << (INTEGER - 6)) | (1L << (FLOAT - 6)) | (1L << (BOLEAN - 6)) | (1L << (LSTRING - 6)))) != 0)) {
				{
				{
				setState(403);
				element();
				}
				setState(408);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(404);
					match(CM);
					{
					setState(405);
					element();
					}
					}
					}
					setState(410);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(413);
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

	public static class ElementContext extends ParserRuleContext {
		public Array_listContext array_list() {
			return getRuleContext(Array_listContext.class,0);
		}
		public Array_indexContext array_index() {
			return getRuleContext(Array_indexContext.class,0);
		}
		public ElementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element; }
	}

	public final ElementContext element() throws RecognitionException {
		ElementContext _localctx = new ElementContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_element);
		try {
			setState(417);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				setState(415);
				array_list();
				}
				break;
			case INTEGER:
			case FLOAT:
			case BOLEAN:
			case LSTRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(416);
				array_index();
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

	public static class ArraylitContext extends ParserRuleContext {
		public Array_listContext array_list() {
			return getRuleContext(Array_listContext.class,0);
		}
		public ArraylitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arraylit; }
	}

	public final ArraylitContext arraylit() throws RecognitionException {
		ArraylitContext _localctx = new ArraylitContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_arraylit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(419);
			array_list();
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
		case 25:
			return exp1_sempred((Exp1Context)_localctx, predIndex);
		case 26:
			return exp2_sempred((Exp2Context)_localctx, predIndex);
		case 27:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F\u01a8\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\3\2\7\2Z\n\2\f\2\16\2]\13\2\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3"+
		"\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4o\n\4\f\4\16\4r\13\4\3\5\3\5\5\5v\n"+
		"\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0080\n\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\3\t\7\t\u008b\n\t\f\t\16\t\u008e\13\t\3\t\7\t\u0091\n\t\f\t"+
		"\16\t\u0094\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009f\n\n\3\13"+
		"\3\13\3\13\3\13\7\13\u00a5\n\13\f\13\16\13\u00a8\13\13\3\f\3\f\3\f\3\f"+
		"\7\f\u00ae\n\f\f\f\16\f\u00b1\13\f\3\f\3\f\3\f\3\r\3\r\3\r\7\r\u00b9\n"+
		"\r\f\r\16\r\u00bc\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7"+
		"\16\u00c7\n\16\f\16\16\16\u00ca\13\16\3\16\3\16\5\16\u00ce\n\16\3\16\3"+
		"\16\3\16\3\17\3\17\5\17\u00d5\n\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\24\3\24\3\24\3\25\3\25\5\25\u0100\n\25\3\25\3\25\3\26\3\26\3\26"+
		"\3\26\3\26\7\26\u0109\n\26\f\26\16\26\u010c\13\26\5\26\u010e\n\26\3\26"+
		"\3\26\3\27\3\27\3\27\3\30\3\30\5\30\u0117\n\30\3\30\3\30\3\30\3\30\6\30"+
		"\u011d\n\30\r\30\16\30\u011e\3\31\3\31\3\32\3\32\3\32\3\32\3\32\5\32\u0128"+
		"\n\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0130\n\33\f\33\16\33\u0133\13"+
		"\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u013b\n\34\f\34\16\34\u013e\13"+
		"\34\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0146\n\35\f\35\16\35\u0149\13"+
		"\35\3\36\3\36\3\36\5\36\u014e\n\36\3\37\3\37\3\37\5\37\u0153\n\37\3 \3"+
		" \5 \u0157\n \3!\3!\5!\u015b\n!\3\"\3\"\3\"\3\"\3\"\5\"\u0162\n\"\3#\3"+
		"#\5#\u0166\n#\3$\3$\3$\3$\3$\5$\u016d\n$\3%\3%\3%\7%\u0172\n%\f%\16%\u0175"+
		"\13%\3&\3&\3&\7&\u017a\n&\f&\16&\u017d\13&\3\'\3\'\3\'\7\'\u0182\n\'\f"+
		"\'\16\'\u0185\13\'\3(\3(\3(\7(\u018a\n(\f(\16(\u018d\13(\3)\3)\3)\3)\5"+
		")\u0193\n)\3*\3*\3*\3*\7*\u0199\n*\f*\16*\u019c\13*\5*\u019e\n*\3*\3*"+
		"\3+\3+\5+\u01a4\n+\3,\3,\3,\2\5\64\668-\2\4\6\b\n\f\16\20\22\24\26\30"+
		"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTV\2\5\3\2*+\3\2\25\30\3\2"+
		"\27\30\2\u01ae\2[\3\2\2\2\4f\3\2\2\2\6k\3\2\2\2\bu\3\2\2\2\nw\3\2\2\2"+
		"\fy\3\2\2\2\16\u0087\3\2\2\2\20\u008c\3\2\2\2\22\u009e\3\2\2\2\24\u00a0"+
		"\3\2\2\2\26\u00a9\3\2\2\2\30\u00b5\3\2\2\2\32\u00bd\3\2\2\2\34\u00d4\3"+
		"\2\2\2\36\u00da\3\2\2\2 \u00e9\3\2\2\2\"\u00f0\3\2\2\2$\u00f7\3\2\2\2"+
		"&\u00fa\3\2\2\2(\u00fd\3\2\2\2*\u0103\3\2\2\2,\u0111\3\2\2\2.\u0116\3"+
		"\2\2\2\60\u0120\3\2\2\2\62\u0127\3\2\2\2\64\u0129\3\2\2\2\66\u0134\3\2"+
		"\2\28\u013f\3\2\2\2:\u014d\3\2\2\2<\u0152\3\2\2\2>\u0156\3\2\2\2@\u015a"+
		"\3\2\2\2B\u0161\3\2\2\2D\u0165\3\2\2\2F\u016c\3\2\2\2H\u016e\3\2\2\2J"+
		"\u0176\3\2\2\2L\u017e\3\2\2\2N\u0186\3\2\2\2P\u0192\3\2\2\2R\u0194\3\2"+
		"\2\2T\u01a3\3\2\2\2V\u01a5\3\2\2\2XZ\5\4\3\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2"+
		"\2\2[\\\3\2\2\2\\a\3\2\2\2][\3\2\2\2^`\5\f\7\2_^\3\2\2\2`c\3\2\2\2a_\3"+
		"\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7\2\2\3e\3\3\2\2\2fg\7-\2\2gh\7"+
		"\17\2\2hi\5\6\4\2ij\7\16\2\2j\5\3\2\2\2kp\5\b\5\2lm\7\20\2\2mo\5\b\5\2"+
		"nl\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\7\3\2\2\2rp\3\2\2\2sv\5\26\f"+
		"\2tv\5\24\13\2us\3\2\2\2ut\3\2\2\2v\t\3\2\2\2wx\3\2\2\2x\13\3\2\2\2yz"+
		"\7.\2\2z{\7\17\2\2{\177\7\7\2\2|}\7\67\2\2}~\7\17\2\2~\u0080\5\30\r\2"+
		"\177|\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\7/\2\2"+
		"\u0082\u0083\7\17\2\2\u0083\u0084\5\16\b\2\u0084\u0085\7:\2\2\u0085\u0086"+
		"\7\21\2\2\u0086\r\3\2\2\2\u0087\u0088\5\20\t\2\u0088\17\3\2\2\2\u0089"+
		"\u008b\5\4\3\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2"+
		"\2\2\u008c\u008d\3\2\2\2\u008d\u0092\3\2\2\2\u008e\u008c\3\2\2\2\u008f"+
		"\u0091\5\22\n\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3"+
		"\2\2\2\u0092\u0093\3\2\2\2\u0093\21\3\2\2\2\u0094\u0092\3\2\2\2\u0095"+
		"\u009f\5\34\17\2\u0096\u009f\5\32\16\2\u0097\u009f\5\36\20\2\u0098\u009f"+
		"\5 \21\2\u0099\u009f\5\"\22\2\u009a\u009f\5$\23\2\u009b\u009f\5&\24\2"+
		"\u009c\u009f\5,\27\2\u009d\u009f\5(\25\2\u009e\u0095\3\2\2\2\u009e\u0096"+
		"\3\2\2\2\u009e\u0097\3\2\2\2\u009e\u0098\3\2\2\2\u009e\u0099\3\2\2\2\u009e"+
		"\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3\2"+
		"\2\2\u009f\23\3\2\2\2\u00a0\u00a6\7\7\2\2\u00a1\u00a2\7\n\2\2\u00a2\u00a3"+
		"\7\22\2\2\u00a3\u00a5\7\13\2\2\u00a4\u00a1\3\2\2\2\u00a5\u00a8\3\2\2\2"+
		"\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a6"+
		"\3\2\2\2\u00a9\u00af\7\7\2\2\u00aa\u00ab\7\n\2\2\u00ab\u00ac\7\22\2\2"+
		"\u00ac\u00ae\7\13\2\2\u00ad\u00aa\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad"+
		"\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2"+
		"\u00b3\7,\2\2\u00b3\u00b4\5F$\2\u00b4\27\3\2\2\2\u00b5\u00ba\5\24\13\2"+
		"\u00b6\u00b7\7\20\2\2\u00b7\u00b9\5\24\13\2\u00b8\u00b6\3\2\2\2\u00b9"+
		"\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\31\3\2\2"+
		"\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\7\62\2\2\u00be\u00bf\5\60\31\2\u00bf"+
		"\u00c0\7@\2\2\u00c0\u00c8\5\20\t\2\u00c1\u00c2\7\65\2\2\u00c2\u00c3\5"+
		"\60\31\2\u00c3\u00c4\7@\2\2\u00c4\u00c5\5\20\t\2\u00c5\u00c7\3\2\2\2\u00c6"+
		"\u00c1\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2"+
		"\2\2\u00c9\u00cd\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cc\7\60\2\2\u00cc"+
		"\u00ce\5\20\t\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3"+
		"\2\2\2\u00cf\u00d0\7?\2\2\u00d0\u00d1\7\21\2\2\u00d1\33\3\2\2\2\u00d2"+
		"\u00d5\7\7\2\2\u00d3\u00d5\5.\30\2\u00d4\u00d2\3\2\2\2\u00d4\u00d3\3\2"+
		"\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7\7,\2\2\u00d7\u00d8\5\60\31\2\u00d8"+
		"\u00d9\7\16\2\2\u00d9\35\3\2\2\2\u00da\u00db\7;\2\2\u00db\u00dc\7\f\2"+
		"\2\u00dc\u00dd\7\7\2\2\u00dd\u00de\7,\2\2\u00de\u00df\5\60\31\2\u00df"+
		"\u00e0\7\20\2\2\u00e0\u00e1\5\60\31\2\u00e1\u00e2\7\20\2\2\u00e2\u00e3"+
		"\5\64\33\2\u00e3\u00e4\7\r\2\2\u00e4\u00e5\7>\2\2\u00e5\u00e6\5\20\t\2"+
		"\u00e6\u00e7\7\61\2\2\u00e7\u00e8\7\21\2\2\u00e8\37\3\2\2\2\u00e9\u00ea"+
		"\78\2\2\u00ea\u00eb\5\60\31\2\u00eb\u00ec\7>\2\2\u00ec\u00ed\5\20\t\2"+
		"\u00ed\u00ee\7\66\2\2\u00ee\u00ef\7\21\2\2\u00ef!\3\2\2\2\u00f0\u00f1"+
		"\7>\2\2\u00f1\u00f2\5\20\t\2\u00f2\u00f3\78\2\2\u00f3\u00f4\5\60\31\2"+
		"\u00f4\u00f5\7\63\2\2\u00f5\u00f6\7\21\2\2\u00f6#\3\2\2\2\u00f7\u00f8"+
		"\7\64\2\2\u00f8\u00f9\7\16\2\2\u00f9%\3\2\2\2\u00fa\u00fb\79\2\2\u00fb"+
		"\u00fc\7\16\2\2\u00fc\'\3\2\2\2\u00fd\u00ff\7<\2\2\u00fe\u0100\5\60\31"+
		"\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0102"+
		"\7\16\2\2\u0102)\3\2\2\2\u0103\u0104\7\7\2\2\u0104\u010d\7\f\2\2\u0105"+
		"\u010a\5\60\31\2\u0106\u0107\7\20\2\2\u0107\u0109\5\60\31\2\u0108\u0106"+
		"\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b"+
		"\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u0105\3\2\2\2\u010d\u010e\3\2"+
		"\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7\r\2\2\u0110+\3\2\2\2\u0111\u0112"+
		"\5*\26\2\u0112\u0113\7\16\2\2\u0113-\3\2\2\2\u0114\u0117\5*\26\2\u0115"+
		"\u0117\7\7\2\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117\u011c\3\2"+
		"\2\2\u0118\u0119\7\n\2\2\u0119\u011a\5\60\31\2\u011a\u011b\7\13\2\2\u011b"+
		"\u011d\3\2\2\2\u011c\u0118\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011c\3\2"+
		"\2\2\u011e\u011f\3\2\2\2\u011f/\3\2\2\2\u0120\u0121\5\62\32\2\u0121\61"+
		"\3\2\2\2\u0122\u0123\5\64\33\2\u0123\u0124\7\5\2\2\u0124\u0125\5\64\33"+
		"\2\u0125\u0128\3\2\2\2\u0126\u0128\5\64\33\2\u0127\u0122\3\2\2\2\u0127"+
		"\u0126\3\2\2\2\u0128\63\3\2\2\2\u0129\u012a\b\33\1\2\u012a\u012b\5\66"+
		"\34\2\u012b\u0131\3\2\2\2\u012c\u012d\f\4\2\2\u012d\u012e\t\2\2\2\u012e"+
		"\u0130\5\66\34\2\u012f\u012c\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f\3"+
		"\2\2\2\u0131\u0132\3\2\2\2\u0132\65\3\2\2\2\u0133\u0131\3\2\2\2\u0134"+
		"\u0135\b\34\1\2\u0135\u0136\58\35\2\u0136\u013c\3\2\2\2\u0137\u0138\f"+
		"\4\2\2\u0138\u0139\t\3\2\2\u0139\u013b\58\35\2\u013a\u0137\3\2\2\2\u013b"+
		"\u013e\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\67\3\2\2"+
		"\2\u013e\u013c\3\2\2\2\u013f\u0140\b\35\1\2\u0140\u0141\5:\36\2\u0141"+
		"\u0147\3\2\2\2\u0142\u0143\f\4\2\2\u0143\u0144\7\6\2\2\u0144\u0146\5:"+
		"\36\2\u0145\u0142\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2\u0147"+
		"\u0148\3\2\2\2\u01489\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\7)\2\2\u014b"+
		"\u014e\5:\36\2\u014c\u014e\5<\37\2\u014d\u014a\3\2\2\2\u014d\u014c\3\2"+
		"\2\2\u014e;\3\2\2\2\u014f\u0150\t\4\2\2\u0150\u0153\5<\37\2\u0151\u0153"+
		"\5> \2\u0152\u014f\3\2\2\2\u0152\u0151\3\2\2\2\u0153=\3\2\2\2\u0154\u0157"+
		"\5.\30\2\u0155\u0157\5@!\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157"+
		"?\3\2\2\2\u0158\u015b\5*\26\2\u0159\u015b\5B\"\2\u015a\u0158\3\2\2\2\u015a"+
		"\u0159\3\2\2\2\u015bA\3\2\2\2\u015c\u015d\7\f\2\2\u015d\u015e\5\60\31"+
		"\2\u015e\u015f\7\r\2\2\u015f\u0162\3\2\2\2\u0160\u0162\5D#\2\u0161\u015c"+
		"\3\2\2\2\u0161\u0160\3\2\2\2\u0162C\3\2\2\2\u0163\u0166\7\7\2\2\u0164"+
		"\u0166\5F$\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2\u0166E\3\2\2\2\u0167"+
		"\u016d\5V,\2\u0168\u016d\7\22\2\2\u0169\u016d\7\23\2\2\u016a\u016d\7\24"+
		"\2\2\u016b\u016d\7F\2\2\u016c\u0167\3\2\2\2\u016c\u0168\3\2\2\2\u016c"+
		"\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016dG\3\2\2\2"+
		"\u016e\u0173\7\24\2\2\u016f\u0170\7\20\2\2\u0170\u0172\7\24\2\2\u0171"+
		"\u016f\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2"+
		"\2\2\u0174I\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u017b\7\22\2\2\u0177\u0178"+
		"\7\20\2\2\u0178\u017a\7\22\2\2\u0179\u0177\3\2\2\2\u017a\u017d\3\2\2\2"+
		"\u017b\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017cK\3\2\2\2\u017d\u017b\3"+
		"\2\2\2\u017e\u0183\7\23\2\2\u017f\u0180\7\20\2\2\u0180\u0182\7\23\2\2"+
		"\u0181\u017f\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184"+
		"\3\2\2\2\u0184M\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u018b\7F\2\2\u0187\u0188"+
		"\7\20\2\2\u0188\u018a\7F\2\2\u0189\u0187\3\2\2\2\u018a\u018d\3\2\2\2\u018b"+
		"\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cO\3\2\2\2\u018d\u018b\3\2\2\2"+
		"\u018e\u0193\5J&\2\u018f\u0193\5L\'\2\u0190\u0193\5N(\2\u0191\u0193\5"+
		"H%\2\u0192\u018e\3\2\2\2\u0192\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192"+
		"\u0191\3\2\2\2\u0193Q\3\2\2\2\u0194\u019d\7\b\2\2\u0195\u019a\5T+\2\u0196"+
		"\u0197\7\20\2\2\u0197\u0199\5T+\2\u0198\u0196\3\2\2\2\u0199\u019c\3\2"+
		"\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019e\3\2\2\2\u019c"+
		"\u019a\3\2\2\2\u019d\u0195\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\3\2"+
		"\2\2\u019f\u01a0\7\t\2\2\u01a0S\3\2\2\2\u01a1\u01a4\5R*\2\u01a2\u01a4"+
		"\5P)\2\u01a3\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4U\3\2\2\2\u01a5\u01a6"+
		"\5R*\2\u01a6W\3\2\2\2([apu\177\u008c\u0092\u009e\u00a6\u00af\u00ba\u00c8"+
		"\u00cd\u00d4\u00ff\u010a\u010d\u0116\u011e\u0127\u0131\u013c\u0147\u014d"+
		"\u0152\u0156\u015a\u0161\u0165\u016c\u0173\u017b\u0183\u018b\u0192\u019a"+
		"\u019d\u01a3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}