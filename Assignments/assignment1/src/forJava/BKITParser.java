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
		ID=1, REL_OP=2, BIN_LOGICAL_OP=3, ADD_OP=4, MUL_OP=5, UN_LOGICAL_OP=6, 
		UN_OP=7, INT_LIT=8, FLOAT_LIT=9, BOOL_LIT=10, STRING_LIT=11, BODY=12, 
		BREAK=13, CONTINUE=14, DO=15, ELSE=16, ELSEIF=17, ENDIF=18, ENDBODY=19, 
		ENDFOR=20, ENDWHILE=21, FOR=22, FUNCTION=23, IF=24, PARAMETER=25, RETURN=26, 
		THEN=27, VAR=28, WHILE=29, TRUE=30, FALSE=31, ENDDO=32, PLUS_INT=33, PLUS_FLOAT=34, 
		MINUS_INT=35, MINUS_FLOAT=36, STAR_INT=37, STAR_FLOAT=38, DIV_INT=39, 
		DIV_FLOAT=40, MOD=41, NOT=42, AND=43, OR=44, EQUAL=45, NOT_EQUAL_INT=46, 
		LESS_INT=47, GREATER_INT=48, LESS_OR_EQUAL_INT=49, GREATER_OR_EQUAL_INT=50, 
		NOT_EQUAL_FLOAT=51, LESS_FLOAT=52, GREATER_FLOAT=53, LESS_OR_EQUAL_FLOAT=54, 
		GREATER_OR_EQUAL_FLOAT=55, LEFT_PAREN=56, RIGHT_PAREN=57, LEFT_BRACKET=58, 
		RIGHT_BRACKET=59, LEFT_BRACE=60, RIGHT_BRACE=61, COLON=62, DOT=63, SEMI=64, 
		COMMA=65, ASSIGN=66, DOUBLE_QUOTE=67, INT_OF_FLOAT=68, INT_OF_STRING=69, 
		FLOAT_TO_INT=70, FLOAT_OF_STRING=71, BOOL_OF_STRING=72, STRING_OF_BOOL=73, 
		STRING_OF_INT=74, STRING_OF_FLOAT=75, COMMENT=76, WS=77, ILLEGAL_ESCAPE=78, 
		UNCLOSE_STRING=79, UNTERMINATED_COMMENT=80, ERROR_CHAR=81;
	public static final int
		RULE_program = 0, RULE_var_declare = 1, RULE_function_declare = 2, RULE_stmt_list = 3, 
		RULE_stmt = 4, RULE_if_stmt = 5, RULE_var_declare_stmt = 6, RULE_for_stmt = 7, 
		RULE_while_stmt = 8, RULE_dowhile_stmt = 9, RULE_assign_stmt = 10, RULE_break_stmt = 11, 
		RULE_continue_stmt = 12, RULE_call_stmt = 13, RULE_return_stmt = 14, RULE_expr = 15, 
		RULE_expr1 = 16, RULE_expr2 = 17, RULE_expr3 = 18, RULE_expr4 = 19, RULE_expr5 = 20, 
		RULE_expr6 = 21, RULE_array_cell = 22, RULE_expr7 = 23, RULE_expr8 = 24, 
		RULE_operand = 25, RULE_function_call = 26, RULE_index_op = 27, RULE_array = 28, 
		RULE_primitive_data = 29, RULE_array_lit = 30, RULE_var_list = 31, RULE_var_init = 32, 
		RULE_var_non_init = 33, RULE_composite_var = 34, RULE_composite_init = 35, 
		RULE_primitive_init = 36, RULE_params_list = 37;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "var_declare", "function_declare", "stmt_list", "stmt", "if_stmt", 
			"var_declare_stmt", "for_stmt", "while_stmt", "dowhile_stmt", "assign_stmt", 
			"break_stmt", "continue_stmt", "call_stmt", "return_stmt", "expr", "expr1", 
			"expr2", "expr3", "expr4", "expr5", "expr6", "array_cell", "expr7", "expr8", 
			"operand", "function_call", "index_op", "array", "primitive_data", "array_lit", 
			"var_list", "var_init", "var_non_init", "composite_var", "composite_init", 
			"primitive_init", "params_list"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndIf'", 
			"'EndBody'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
			"'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", "'True'", "'False'", 
			"'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", 
			"'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
			"'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
			"'{'", "'}'", "':'", "'.'", "';'", "','", "'='", "'\"'", "'int_of_float'", 
			"'int_of_string'", "'float_to_int'", "'float_of_string'", "'bool_of_string'", 
			"'string_of_bool'", "'string_of_int'", "'string_of_float'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ID", "REL_OP", "BIN_LOGICAL_OP", "ADD_OP", "MUL_OP", "UN_LOGICAL_OP", 
			"UN_OP", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "BODY", "BREAK", 
			"CONTINUE", "DO", "ELSE", "ELSEIF", "ENDIF", "ENDBODY", "ENDFOR", "ENDWHILE", 
			"FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
			"TRUE", "FALSE", "ENDDO", "PLUS_INT", "PLUS_FLOAT", "MINUS_INT", "MINUS_FLOAT", 
			"STAR_INT", "STAR_FLOAT", "DIV_INT", "DIV_FLOAT", "MOD", "NOT", "AND", 
			"OR", "EQUAL", "NOT_EQUAL_INT", "LESS_INT", "GREATER_INT", "LESS_OR_EQUAL_INT", 
			"GREATER_OR_EQUAL_INT", "NOT_EQUAL_FLOAT", "LESS_FLOAT", "GREATER_FLOAT", 
			"LESS_OR_EQUAL_FLOAT", "GREATER_OR_EQUAL_FLOAT", "LEFT_PAREN", "RIGHT_PAREN", 
			"LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "COLON", 
			"DOT", "SEMI", "COMMA", "ASSIGN", "DOUBLE_QUOTE", "INT_OF_FLOAT", "INT_OF_STRING", 
			"FLOAT_TO_INT", "FLOAT_OF_STRING", "BOOL_OF_STRING", "STRING_OF_BOOL", 
			"STRING_OF_INT", "STRING_OF_FLOAT", "COMMENT", "WS", "ILLEGAL_ESCAPE", 
			"UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR"
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
		public List<Var_declareContext> var_declare() {
			return getRuleContexts(Var_declareContext.class);
		}
		public Var_declareContext var_declare(int i) {
			return getRuleContext(Var_declareContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
		}
		public List<Function_declareContext> function_declare() {
			return getRuleContexts(Function_declareContext.class);
		}
		public Function_declareContext function_declare(int i) {
			return getRuleContext(Function_declareContext.class,i);
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
			setState(81);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(76);
				var_declare();
				setState(77);
				match(SEMI);
				}
				}
				setState(83);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCTION) {
				{
				{
				setState(84);
				function_declare();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
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
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(VAR);
			setState(93);
			match(COLON);
			setState(94);
			var_list();
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

	public static class Function_declareContext extends ParserRuleContext {
		public TerminalNode FUNCTION() { return getToken(BKITParser.FUNCTION, 0); }
		public List<TerminalNode> COLON() { return getTokens(BKITParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(BKITParser.COLON, i);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode BODY() { return getToken(BKITParser.BODY, 0); }
		public TerminalNode ENDBODY() { return getToken(BKITParser.ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public TerminalNode PARAMETER() { return getToken(BKITParser.PARAMETER, 0); }
		public Params_listContext params_list() {
			return getRuleContext(Params_listContext.class,0);
		}
		public List<Var_declare_stmtContext> var_declare_stmt() {
			return getRuleContexts(Var_declare_stmtContext.class);
		}
		public Var_declare_stmtContext var_declare_stmt(int i) {
			return getRuleContext(Var_declare_stmtContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public Function_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declare; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_declare(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_declare(this);
		}
	}

	public final Function_declareContext function_declare() throws RecognitionException {
		Function_declareContext _localctx = new Function_declareContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(96);
			match(FUNCTION);
			setState(97);
			match(COLON);
			setState(98);
			match(ID);
			setState(102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARAMETER) {
				{
				setState(99);
				match(PARAMETER);
				setState(100);
				match(COLON);
				setState(101);
				params_list();
				}
			}

			setState(104);
			match(BODY);
			setState(105);
			match(COLON);
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(106);
				var_declare_stmt();
				setState(107);
				match(SEMI);
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << BREAK) | (1L << CONTINUE) | (1L << DO) | (1L << FOR) | (1L << IF) | (1L << RETURN) | (1L << WHILE) | (1L << LEFT_PAREN) | (1L << LEFT_BRACE))) != 0)) {
				{
				{
				setState(114);
				stmt();
				}
				}
				setState(119);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(120);
			match(ENDBODY);
			setState(121);
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

	public static class Stmt_listContext extends ParserRuleContext {
		public List<Var_declare_stmtContext> var_declare_stmt() {
			return getRuleContexts(Var_declare_stmtContext.class);
		}
		public Var_declare_stmtContext var_declare_stmt(int i) {
			return getRuleContext(Var_declare_stmtContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(BKITParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(BKITParser.SEMI, i);
		}
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public Stmt_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStmt_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStmt_list(this);
		}
	}

	public final Stmt_listContext stmt_list() throws RecognitionException {
		Stmt_listContext _localctx = new Stmt_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_stmt_list);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VAR) {
				{
				{
				setState(123);
				var_declare_stmt();
				setState(124);
				match(SEMI);
				}
				}
				setState(130);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(134);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(131);
					stmt();
					}
					} 
				}
				setState(136);
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

	public static class StmtContext extends ParserRuleContext {
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_stmtContext for_stmt() {
			return getRuleContext(For_stmtContext.class,0);
		}
		public While_stmtContext while_stmt() {
			return getRuleContext(While_stmtContext.class,0);
		}
		public Dowhile_stmtContext dowhile_stmt() {
			return getRuleContext(Dowhile_stmtContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(BKITParser.SEMI, 0); }
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
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_stmt);
		try {
			setState(156);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				if_stmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				for_stmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(139);
				while_stmt();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(140);
				dowhile_stmt();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(141);
				assign_stmt();
				setState(142);
				match(SEMI);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(144);
				break_stmt();
				setState(145);
				match(SEMI);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(147);
				continue_stmt();
				setState(148);
				match(SEMI);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(150);
				call_stmt();
				setState(151);
				match(SEMI);
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(153);
				return_stmt();
				setState(154);
				match(SEMI);
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

	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(BKITParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> THEN() { return getTokens(BKITParser.THEN); }
		public TerminalNode THEN(int i) {
			return getToken(BKITParser.THEN, i);
		}
		public List<Stmt_listContext> stmt_list() {
			return getRuleContexts(Stmt_listContext.class);
		}
		public Stmt_listContext stmt_list(int i) {
			return getRuleContext(Stmt_listContext.class,i);
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
		enterRule(_localctx, 10, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(IF);
			setState(159);
			expr();
			setState(160);
			match(THEN);
			setState(161);
			stmt_list();
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(162);
				match(ELSEIF);
				setState(163);
				expr();
				setState(164);
				match(THEN);
				setState(165);
				stmt_list();
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(172);
				match(ELSE);
				setState(173);
				stmt_list();
				}
			}

			setState(176);
			match(ENDIF);
			setState(177);
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

	public static class Var_declare_stmtContext extends ParserRuleContext {
		public Var_declareContext var_declare() {
			return getRuleContext(Var_declareContext.class,0);
		}
		public Var_declare_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_declare_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVar_declare_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVar_declare_stmt(this);
		}
	}

	public final Var_declare_stmtContext var_declare_stmt() throws RecognitionException {
		Var_declare_stmtContext _localctx = new Var_declare_stmtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_var_declare_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(179);
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

	public static class For_stmtContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(BKITParser.FOR, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public TerminalNode ENDFOR() { return getToken(BKITParser.ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
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
		enterRule(_localctx, 14, RULE_for_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(FOR);
			setState(182);
			match(LEFT_PAREN);
			setState(183);
			match(ID);
			setState(184);
			match(ASSIGN);
			setState(185);
			expr();
			setState(186);
			match(COMMA);
			setState(187);
			expr();
			setState(188);
			match(COMMA);
			setState(189);
			expr();
			setState(190);
			match(RIGHT_PAREN);
			setState(191);
			match(DO);
			setState(192);
			stmt_list();
			setState(193);
			match(ENDFOR);
			setState(194);
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
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
		enterRule(_localctx, 16, RULE_while_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(WHILE);
			setState(197);
			expr();
			setState(198);
			match(DO);
			setState(199);
			stmt_list();
			setState(200);
			match(ENDWHILE);
			setState(201);
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

	public static class Dowhile_stmtContext extends ParserRuleContext {
		public TerminalNode DO() { return getToken(BKITParser.DO, 0); }
		public Stmt_listContext stmt_list() {
			return getRuleContext(Stmt_listContext.class,0);
		}
		public TerminalNode WHILE() { return getToken(BKITParser.WHILE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ENDDO() { return getToken(BKITParser.ENDDO, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public Dowhile_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dowhile_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterDowhile_stmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitDowhile_stmt(this);
		}
	}

	public final Dowhile_stmtContext dowhile_stmt() throws RecognitionException {
		Dowhile_stmtContext _localctx = new Dowhile_stmtContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_dowhile_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(203);
			match(DO);
			setState(204);
			stmt_list();
			setState(205);
			match(WHILE);
			setState(206);
			expr();
			setState(207);
			match(ENDDO);
			setState(208);
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
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Array_cellContext array_cell() {
			return getRuleContext(Array_cellContext.class,0);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
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
		enterRule(_localctx, 20, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(210);
				array_cell();
				}
				break;
			case 2:
				{
				setState(211);
				match(ID);
				}
				break;
			}
			setState(214);
			match(ASSIGN);
			setState(215);
			expr();
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
		enterRule(_localctx, 22, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(BREAK);
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
		enterRule(_localctx, 24, RULE_continue_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(CONTINUE);
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
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
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
		enterRule(_localctx, 26, RULE_call_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			match(ID);
			setState(222);
			match(LEFT_PAREN);
			setState(233);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << UN_LOGICAL_OP) | (1L << UN_OP) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << LEFT_PAREN) | (1L << LEFT_BRACE))) != 0)) {
				{
				{
				setState(223);
				expr();
				setState(228);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(224);
					match(COMMA);
					setState(225);
					expr();
					}
					}
					setState(230);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(235);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(236);
			match(RIGHT_PAREN);
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
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
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
		enterRule(_localctx, 28, RULE_return_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			match(RETURN);
			setState(240);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << UN_LOGICAL_OP) | (1L << UN_OP) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << LEFT_PAREN) | (1L << LEFT_BRACE))) != 0)) {
				{
				setState(239);
				expr();
				}
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

	public static class ExprContext extends ParserRuleContext {
		public List<Expr1Context> expr1() {
			return getRuleContexts(Expr1Context.class);
		}
		public Expr1Context expr1(int i) {
			return getRuleContext(Expr1Context.class,i);
		}
		public TerminalNode REL_OP() { return getToken(BKITParser.REL_OP, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_expr);
		try {
			setState(247);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(242);
				expr1(0);
				setState(243);
				match(REL_OP);
				setState(244);
				expr1(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(246);
				expr1(0);
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

	public static class Expr1Context extends ParserRuleContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public Expr1Context expr1() {
			return getRuleContext(Expr1Context.class,0);
		}
		public TerminalNode BIN_LOGICAL_OP() { return getToken(BKITParser.BIN_LOGICAL_OP, 0); }
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr1(this);
		}
	}

	public final Expr1Context expr1() throws RecognitionException {
		return expr1(0);
	}

	private Expr1Context expr1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr1Context _localctx = new Expr1Context(_ctx, _parentState);
		Expr1Context _prevctx = _localctx;
		int _startState = 32;
		enterRecursionRule(_localctx, 32, RULE_expr1, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(250);
			expr2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(257);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr1Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr1);
					setState(252);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(253);
					match(BIN_LOGICAL_OP);
					setState(254);
					expr2(0);
					}
					} 
				}
				setState(259);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
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

	public static class Expr2Context extends ParserRuleContext {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public TerminalNode ADD_OP() { return getToken(BKITParser.ADD_OP, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr2(this);
		}
	}

	public final Expr2Context expr2() throws RecognitionException {
		return expr2(0);
	}

	private Expr2Context expr2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr2Context _localctx = new Expr2Context(_ctx, _parentState);
		Expr2Context _prevctx = _localctx;
		int _startState = 34;
		enterRecursionRule(_localctx, 34, RULE_expr2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(261);
			expr3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(268);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr2Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr2);
					setState(263);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(264);
					match(ADD_OP);
					setState(265);
					expr3(0);
					}
					} 
				}
				setState(270);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,16,_ctx);
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

	public static class Expr3Context extends ParserRuleContext {
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public TerminalNode MUL_OP() { return getToken(BKITParser.MUL_OP, 0); }
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr3(this);
		}
	}

	public final Expr3Context expr3() throws RecognitionException {
		return expr3(0);
	}

	private Expr3Context expr3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Expr3Context _localctx = new Expr3Context(_ctx, _parentState);
		Expr3Context _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr3, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(272);
			expr4();
			}
			_ctx.stop = _input.LT(-1);
			setState(279);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Expr3Context(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr3);
					setState(274);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(275);
					match(MUL_OP);
					setState(276);
					expr4();
					}
					} 
				}
				setState(281);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
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

	public static class Expr4Context extends ParserRuleContext {
		public TerminalNode UN_LOGICAL_OP() { return getToken(BKITParser.UN_LOGICAL_OP, 0); }
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr4(this);
		}
	}

	public final Expr4Context expr4() throws RecognitionException {
		Expr4Context _localctx = new Expr4Context(_ctx, getState());
		enterRule(_localctx, 38, RULE_expr4);
		try {
			setState(285);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case UN_LOGICAL_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(282);
				match(UN_LOGICAL_OP);
				setState(283);
				expr4();
				}
				break;
			case ID:
			case UN_OP:
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
			case LEFT_PAREN:
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(284);
				expr5();
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

	public static class Expr5Context extends ParserRuleContext {
		public TerminalNode UN_OP() { return getToken(BKITParser.UN_OP, 0); }
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr5; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr5(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr5(this);
		}
	}

	public final Expr5Context expr5() throws RecognitionException {
		Expr5Context _localctx = new Expr5Context(_ctx, getState());
		enterRule(_localctx, 40, RULE_expr5);
		try {
			setState(290);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case UN_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(287);
				match(UN_OP);
				setState(288);
				expr5();
				}
				break;
			case ID:
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
			case LEFT_PAREN:
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 2);
				{
				setState(289);
				expr6();
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

	public static class Expr6Context extends ParserRuleContext {
		public Array_cellContext array_cell() {
			return getRuleContext(Array_cellContext.class,0);
		}
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public Expr6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr6; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr6(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr6(this);
		}
	}

	public final Expr6Context expr6() throws RecognitionException {
		Expr6Context _localctx = new Expr6Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_expr6);
		try {
			setState(294);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				array_cell();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
				expr7();
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

	public static class Array_cellContext extends ParserRuleContext {
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(BKITParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(BKITParser.LEFT_BRACKET, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(BKITParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(BKITParser.RIGHT_BRACKET, i);
		}
		public Array_cellContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_cell; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray_cell(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray_cell(this);
		}
	}

	public final Array_cellContext array_cell() throws RecognitionException {
		Array_cellContext _localctx = new Array_cellContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_array_cell);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			expr7();
			setState(301); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(297);
					match(LEFT_BRACKET);
					setState(298);
					expr();
					setState(299);
					match(RIGHT_BRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(303); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
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

	public static class Expr7Context extends ParserRuleContext {
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public Expr7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr7; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr7(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr7(this);
		}
	}

	public final Expr7Context expr7() throws RecognitionException {
		Expr7Context _localctx = new Expr7Context(_ctx, getState());
		enterRule(_localctx, 46, RULE_expr7);
		try {
			setState(307);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(305);
				function_call();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(306);
				expr8();
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

	public static class Expr8Context extends ParserRuleContext {
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public Expr8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr8; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterExpr8(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitExpr8(this);
		}
	}

	public final Expr8Context expr8() throws RecognitionException {
		Expr8Context _localctx = new Expr8Context(_ctx, getState());
		enterRule(_localctx, 48, RULE_expr8);
		try {
			setState(314);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 1);
				{
				setState(309);
				operand();
				}
				break;
			case LEFT_PAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(310);
				match(LEFT_PAREN);
				setState(311);
				expr();
				setState(312);
				match(RIGHT_PAREN);
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
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Primitive_dataContext primitive_data() {
			return getRuleContext(Primitive_dataContext.class,0);
		}
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
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
		enterRule(_localctx, 50, RULE_operand);
		try {
			setState(319);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(316);
				match(ID);
				}
				break;
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(317);
				primitive_data();
				}
				break;
			case LEFT_BRACE:
				enterOuterAlt(_localctx, 3);
				{
				setState(318);
				array_lit();
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

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LEFT_PAREN() { return getToken(BKITParser.LEFT_PAREN, 0); }
		public TerminalNode RIGHT_PAREN() { return getToken(BKITParser.RIGHT_PAREN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterFunction_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitFunction_call(this);
		}
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(321);
			match(ID);
			setState(322);
			match(LEFT_PAREN);
			setState(333);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << ID) | (1L << UN_LOGICAL_OP) | (1L << UN_OP) | (1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << LEFT_PAREN) | (1L << LEFT_BRACE))) != 0)) {
				{
				{
				setState(323);
				expr();
				setState(328);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(324);
					match(COMMA);
					setState(325);
					expr();
					}
					}
					setState(330);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(335);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(336);
			match(RIGHT_PAREN);
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
		public TerminalNode LEFT_BRACKET() { return getToken(BKITParser.LEFT_BRACKET, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(BKITParser.RIGHT_BRACKET, 0); }
		public Index_opContext index_op() {
			return getRuleContext(Index_opContext.class,0);
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
		enterRule(_localctx, 54, RULE_index_op);
		try {
			setState(347);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(338);
				match(LEFT_BRACKET);
				setState(339);
				expr();
				setState(340);
				match(RIGHT_BRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(342);
				match(LEFT_BRACKET);
				setState(343);
				expr();
				setState(344);
				match(RIGHT_BRACKET);
				setState(345);
				index_op();
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

	public static class ArrayContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray(this);
		}
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(349);
			match(ID);
			setState(350);
			match(ASSIGN);
			setState(351);
			array_lit();
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

	public static class Primitive_dataContext extends ParserRuleContext {
		public TerminalNode INT_LIT() { return getToken(BKITParser.INT_LIT, 0); }
		public TerminalNode FLOAT_LIT() { return getToken(BKITParser.FLOAT_LIT, 0); }
		public TerminalNode STRING_LIT() { return getToken(BKITParser.STRING_LIT, 0); }
		public TerminalNode BOOL_LIT() { return getToken(BKITParser.BOOL_LIT, 0); }
		public Primitive_dataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_data; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterPrimitive_data(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitPrimitive_data(this);
		}
	}

	public final Primitive_dataContext primitive_data() throws RecognitionException {
		Primitive_dataContext _localctx = new Primitive_dataContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_primitive_data);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
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

	public static class Array_litContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACE() { return getToken(BKITParser.LEFT_BRACE, 0); }
		public TerminalNode RIGHT_BRACE() { return getToken(BKITParser.RIGHT_BRACE, 0); }
		public List<Primitive_dataContext> primitive_data() {
			return getRuleContexts(Primitive_dataContext.class);
		}
		public Primitive_dataContext primitive_data(int i) {
			return getRuleContext(Primitive_dataContext.class,i);
		}
		public List<Array_litContext> array_lit() {
			return getRuleContexts(Array_litContext.class);
		}
		public Array_litContext array_lit(int i) {
			return getRuleContext(Array_litContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Array_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_lit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterArray_lit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitArray_lit(this);
		}
	}

	public final Array_litContext array_lit() throws RecognitionException {
		Array_litContext _localctx = new Array_litContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_array_lit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(355);
			match(LEFT_BRACE);
			setState(370);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT_LIT) | (1L << FLOAT_LIT) | (1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << LEFT_BRACE))) != 0)) {
				{
				setState(358);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INT_LIT:
				case FLOAT_LIT:
				case BOOL_LIT:
				case STRING_LIT:
					{
					setState(356);
					primitive_data();
					}
					break;
				case LEFT_BRACE:
					{
					setState(357);
					array_lit();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(367);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(360);
					match(COMMA);
					setState(363);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case INT_LIT:
					case FLOAT_LIT:
					case BOOL_LIT:
					case STRING_LIT:
						{
						setState(361);
						primitive_data();
						}
						break;
					case LEFT_BRACE:
						{
						setState(362);
						array_lit();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					}
					}
					setState(369);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(372);
			match(RIGHT_BRACE);
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
		public List<Var_non_initContext> var_non_init() {
			return getRuleContexts(Var_non_initContext.class);
		}
		public Var_non_initContext var_non_init(int i) {
			return getRuleContext(Var_non_initContext.class,i);
		}
		public List<Var_initContext> var_init() {
			return getRuleContexts(Var_initContext.class);
		}
		public Var_initContext var_init(int i) {
			return getRuleContext(Var_initContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
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
		enterRule(_localctx, 62, RULE_var_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				{
				setState(374);
				var_non_init();
				}
				break;
			case 2:
				{
				setState(375);
				var_init();
				}
				break;
			}
			setState(385);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(378);
				match(COMMA);
				setState(381);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
				case 1:
					{
					setState(379);
					var_non_init();
					}
					break;
				case 2:
					{
					setState(380);
					var_init();
					}
					break;
				}
				}
				}
				setState(387);
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
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public Primitive_dataContext primitive_data() {
			return getRuleContext(Primitive_dataContext.class,0);
		}
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(BKITParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(BKITParser.LEFT_BRACKET, i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(BKITParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(BKITParser.INT_LIT, i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(BKITParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(BKITParser.RIGHT_BRACKET, i);
		}
		public Var_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVar_init(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVar_init(this);
		}
	}

	public final Var_initContext var_init() throws RecognitionException {
		Var_initContext _localctx = new Var_initContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_var_init);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				{
				setState(388);
				match(ID);
				setState(392); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(389);
					match(LEFT_BRACKET);
					setState(390);
					match(INT_LIT);
					setState(391);
					match(RIGHT_BRACKET);
					}
					}
					setState(394); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LEFT_BRACKET );
				}
				break;
			case 2:
				{
				setState(396);
				match(ID);
				}
				break;
			}
			setState(399);
			match(ASSIGN);
			setState(402);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_BRACE:
				{
				setState(400);
				array_lit();
				}
				break;
			case INT_LIT:
			case FLOAT_LIT:
			case BOOL_LIT:
			case STRING_LIT:
				{
				setState(401);
				primitive_data();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Var_non_initContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(BKITParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(BKITParser.LEFT_BRACKET, i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(BKITParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(BKITParser.INT_LIT, i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(BKITParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(BKITParser.RIGHT_BRACKET, i);
		}
		public Var_non_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_non_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVar_non_init(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVar_non_init(this);
		}
	}

	public final Var_non_initContext var_non_init() throws RecognitionException {
		Var_non_initContext _localctx = new Var_non_initContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_var_non_init);
		int _la;
		try {
			setState(413);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(404);
				match(ID);
				setState(408); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(405);
					match(LEFT_BRACKET);
					setState(406);
					match(INT_LIT);
					setState(407);
					match(RIGHT_BRACKET);
					}
					}
					setState(410); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LEFT_BRACKET );
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(412);
				match(ID);
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

	public static class Composite_varContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(BKITParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(BKITParser.LEFT_BRACKET, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(BKITParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(BKITParser.RIGHT_BRACKET, i);
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
		enterRule(_localctx, 68, RULE_composite_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(415);
			match(ID);
			setState(420); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(416);
				match(LEFT_BRACKET);
				setState(417);
				expr();
				setState(418);
				match(RIGHT_BRACKET);
				}
				}
				setState(422); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==LEFT_BRACKET );
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
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
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
		enterRule(_localctx, 70, RULE_composite_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			composite_var();
			setState(425);
			match(ASSIGN);
			setState(426);
			array_lit();
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

	public static class Primitive_initContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public Primitive_dataContext primitive_data() {
			return getRuleContext(Primitive_dataContext.class,0);
		}
		public Primitive_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_init; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterPrimitive_init(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitPrimitive_init(this);
		}
	}

	public final Primitive_initContext primitive_init() throws RecognitionException {
		Primitive_initContext _localctx = new Primitive_initContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_primitive_init);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(428);
			match(ID);
			setState(429);
			match(ASSIGN);
			setState(430);
			primitive_data();
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

	public static class Params_listContext extends ParserRuleContext {
		public List<Var_non_initContext> var_non_init() {
			return getRuleContexts(Var_non_initContext.class);
		}
		public Var_non_initContext var_non_init(int i) {
			return getRuleContext(Var_non_initContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(BKITParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(BKITParser.COMMA, i);
		}
		public Params_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterParams_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitParams_list(this);
		}
	}

	public final Params_listContext params_list() throws RecognitionException {
		Params_listContext _localctx = new Params_listContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_params_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(432);
			var_non_init();
			setState(437);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(433);
				match(COMMA);
				setState(434);
				var_non_init();
				}
				}
				setState(439);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 16:
			return expr1_sempred((Expr1Context)_localctx, predIndex);
		case 17:
			return expr2_sempred((Expr2Context)_localctx, predIndex);
		case 18:
			return expr3_sempred((Expr3Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr1_sempred(Expr1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr2_sempred(Expr2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expr3_sempred(Expr3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S\u01bb\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\2\7\2R\n\2\f\2\16"+
		"\2U\13\2\3\2\7\2X\n\2\f\2\16\2[\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\5\4i\n\4\3\4\3\4\3\4\3\4\3\4\7\4p\n\4\f\4\16\4s\13\4\3"+
		"\4\7\4v\n\4\f\4\16\4y\13\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5\u0081\n\5\f\5\16"+
		"\5\u0084\13\5\3\5\7\5\u0087\n\5\f\5\16\5\u008a\13\5\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u009f\n"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00aa\n\7\f\7\16\7\u00ad\13"+
		"\7\3\7\3\7\5\7\u00b1\n\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\5\f\u00d7\n\f\3\f\3\f\3\f\3\r\3\r"+
		"\3\16\3\16\3\17\3\17\3\17\3\17\3\17\7\17\u00e5\n\17\f\17\16\17\u00e8\13"+
		"\17\7\17\u00ea\n\17\f\17\16\17\u00ed\13\17\3\17\3\17\3\20\3\20\5\20\u00f3"+
		"\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00fa\n\21\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\7\22\u0102\n\22\f\22\16\22\u0105\13\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\7\23\u010d\n\23\f\23\16\23\u0110\13\23\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\7\24\u0118\n\24\f\24\16\24\u011b\13\24\3\25\3\25\3\25\5\25\u0120"+
		"\n\25\3\26\3\26\3\26\5\26\u0125\n\26\3\27\3\27\5\27\u0129\n\27\3\30\3"+
		"\30\3\30\3\30\3\30\6\30\u0130\n\30\r\30\16\30\u0131\3\31\3\31\5\31\u0136"+
		"\n\31\3\32\3\32\3\32\3\32\3\32\5\32\u013d\n\32\3\33\3\33\3\33\5\33\u0142"+
		"\n\33\3\34\3\34\3\34\3\34\3\34\7\34\u0149\n\34\f\34\16\34\u014c\13\34"+
		"\7\34\u014e\n\34\f\34\16\34\u0151\13\34\3\34\3\34\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\35\5\35\u015e\n\35\3\36\3\36\3\36\3\36\3\37\3\37"+
		"\3 \3 \3 \5 \u0169\n \3 \3 \3 \5 \u016e\n \7 \u0170\n \f \16 \u0173\13"+
		" \5 \u0175\n \3 \3 \3!\3!\5!\u017b\n!\3!\3!\3!\5!\u0180\n!\7!\u0182\n"+
		"!\f!\16!\u0185\13!\3\"\3\"\3\"\3\"\6\"\u018b\n\"\r\"\16\"\u018c\3\"\5"+
		"\"\u0190\n\"\3\"\3\"\3\"\5\"\u0195\n\"\3#\3#\3#\3#\6#\u019b\n#\r#\16#"+
		"\u019c\3#\5#\u01a0\n#\3$\3$\3$\3$\3$\6$\u01a7\n$\r$\16$\u01a8\3%\3%\3"+
		"%\3%\3&\3&\3&\3&\3\'\3\'\3\'\7\'\u01b6\n\'\f\'\16\'\u01b9\13\'\3\'\2\5"+
		"\"$&(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>"+
		"@BDFHJL\2\3\3\2\n\r\2\u01c6\2S\3\2\2\2\4^\3\2\2\2\6b\3\2\2\2\b\u0082\3"+
		"\2\2\2\n\u009e\3\2\2\2\f\u00a0\3\2\2\2\16\u00b5\3\2\2\2\20\u00b7\3\2\2"+
		"\2\22\u00c6\3\2\2\2\24\u00cd\3\2\2\2\26\u00d6\3\2\2\2\30\u00db\3\2\2\2"+
		"\32\u00dd\3\2\2\2\34\u00df\3\2\2\2\36\u00f0\3\2\2\2 \u00f9\3\2\2\2\"\u00fb"+
		"\3\2\2\2$\u0106\3\2\2\2&\u0111\3\2\2\2(\u011f\3\2\2\2*\u0124\3\2\2\2,"+
		"\u0128\3\2\2\2.\u012a\3\2\2\2\60\u0135\3\2\2\2\62\u013c\3\2\2\2\64\u0141"+
		"\3\2\2\2\66\u0143\3\2\2\28\u015d\3\2\2\2:\u015f\3\2\2\2<\u0163\3\2\2\2"+
		">\u0165\3\2\2\2@\u017a\3\2\2\2B\u018f\3\2\2\2D\u019f\3\2\2\2F\u01a1\3"+
		"\2\2\2H\u01aa\3\2\2\2J\u01ae\3\2\2\2L\u01b2\3\2\2\2NO\5\4\3\2OP\7B\2\2"+
		"PR\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TY\3\2\2\2US\3\2\2\2"+
		"VX\5\6\4\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2"+
		"\2\\]\7\2\2\3]\3\3\2\2\2^_\7\36\2\2_`\7@\2\2`a\5@!\2a\5\3\2\2\2bc\7\31"+
		"\2\2cd\7@\2\2dh\7\3\2\2ef\7\33\2\2fg\7@\2\2gi\5L\'\2he\3\2\2\2hi\3\2\2"+
		"\2ij\3\2\2\2jk\7\16\2\2kq\7@\2\2lm\5\16\b\2mn\7B\2\2np\3\2\2\2ol\3\2\2"+
		"\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rw\3\2\2\2sq\3\2\2\2tv\5\n\6\2ut\3\2\2"+
		"\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2xz\3\2\2\2yw\3\2\2\2z{\7\25\2\2{|\7A\2"+
		"\2|\7\3\2\2\2}~\5\16\b\2~\177\7B\2\2\177\u0081\3\2\2\2\u0080}\3\2\2\2"+
		"\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0088"+
		"\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0087\5\n\6\2\u0086\u0085\3\2\2\2\u0087"+
		"\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\t\3\2\2\2"+
		"\u008a\u0088\3\2\2\2\u008b\u009f\5\f\7\2\u008c\u009f\5\20\t\2\u008d\u009f"+
		"\5\22\n\2\u008e\u009f\5\24\13\2\u008f\u0090\5\26\f\2\u0090\u0091\7B\2"+
		"\2\u0091\u009f\3\2\2\2\u0092\u0093\5\30\r\2\u0093\u0094\7B\2\2\u0094\u009f"+
		"\3\2\2\2\u0095\u0096\5\32\16\2\u0096\u0097\7B\2\2\u0097\u009f\3\2\2\2"+
		"\u0098\u0099\5\34\17\2\u0099\u009a\7B\2\2\u009a\u009f\3\2\2\2\u009b\u009c"+
		"\5\36\20\2\u009c\u009d\7B\2\2\u009d\u009f\3\2\2\2\u009e\u008b\3\2\2\2"+
		"\u009e\u008c\3\2\2\2\u009e\u008d\3\2\2\2\u009e\u008e\3\2\2\2\u009e\u008f"+
		"\3\2\2\2\u009e\u0092\3\2\2\2\u009e\u0095\3\2\2\2\u009e\u0098\3\2\2\2\u009e"+
		"\u009b\3\2\2\2\u009f\13\3\2\2\2\u00a0\u00a1\7\32\2\2\u00a1\u00a2\5 \21"+
		"\2\u00a2\u00a3\7\35\2\2\u00a3\u00ab\5\b\5\2\u00a4\u00a5\7\23\2\2\u00a5"+
		"\u00a6\5 \21\2\u00a6\u00a7\7\35\2\2\u00a7\u00a8\5\b\5\2\u00a8\u00aa\3"+
		"\2\2\2\u00a9\u00a4\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab"+
		"\u00ac\3\2\2\2\u00ac\u00b0\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\7\22"+
		"\2\2\u00af\u00b1\5\b\5\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1"+
		"\u00b2\3\2\2\2\u00b2\u00b3\7\24\2\2\u00b3\u00b4\7A\2\2\u00b4\r\3\2\2\2"+
		"\u00b5\u00b6\5\4\3\2\u00b6\17\3\2\2\2\u00b7\u00b8\7\30\2\2\u00b8\u00b9"+
		"\7:\2\2\u00b9\u00ba\7\3\2\2\u00ba\u00bb\7D\2\2\u00bb\u00bc\5 \21\2\u00bc"+
		"\u00bd\7C\2\2\u00bd\u00be\5 \21\2\u00be\u00bf\7C\2\2\u00bf\u00c0\5 \21"+
		"\2\u00c0\u00c1\7;\2\2\u00c1\u00c2\7\21\2\2\u00c2\u00c3\5\b\5\2\u00c3\u00c4"+
		"\7\26\2\2\u00c4\u00c5\7A\2\2\u00c5\21\3\2\2\2\u00c6\u00c7\7\37\2\2\u00c7"+
		"\u00c8\5 \21\2\u00c8\u00c9\7\21\2\2\u00c9\u00ca\5\b\5\2\u00ca\u00cb\7"+
		"\27\2\2\u00cb\u00cc\7A\2\2\u00cc\23\3\2\2\2\u00cd\u00ce\7\21\2\2\u00ce"+
		"\u00cf\5\b\5\2\u00cf\u00d0\7\37\2\2\u00d0\u00d1\5 \21\2\u00d1\u00d2\7"+
		"\"\2\2\u00d2\u00d3\7A\2\2\u00d3\25\3\2\2\2\u00d4\u00d7\5.\30\2\u00d5\u00d7"+
		"\7\3\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8"+
		"\u00d9\7D\2\2\u00d9\u00da\5 \21\2\u00da\27\3\2\2\2\u00db\u00dc\7\17\2"+
		"\2\u00dc\31\3\2\2\2\u00dd\u00de\7\20\2\2\u00de\33\3\2\2\2\u00df\u00e0"+
		"\7\3\2\2\u00e0\u00eb\7:\2\2\u00e1\u00e6\5 \21\2\u00e2\u00e3\7C\2\2\u00e3"+
		"\u00e5\5 \21\2\u00e4\u00e2\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2"+
		"\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9"+
		"\u00e1\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2"+
		"\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef\7;\2\2\u00ef"+
		"\35\3\2\2\2\u00f0\u00f2\7\34\2\2\u00f1\u00f3\5 \21\2\u00f2\u00f1\3\2\2"+
		"\2\u00f2\u00f3\3\2\2\2\u00f3\37\3\2\2\2\u00f4\u00f5\5\"\22\2\u00f5\u00f6"+
		"\7\4\2\2\u00f6\u00f7\5\"\22\2\u00f7\u00fa\3\2\2\2\u00f8\u00fa\5\"\22\2"+
		"\u00f9\u00f4\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa!\3\2\2\2\u00fb\u00fc\b"+
		"\22\1\2\u00fc\u00fd\5$\23\2\u00fd\u0103\3\2\2\2\u00fe\u00ff\f\4\2\2\u00ff"+
		"\u0100\7\5\2\2\u0100\u0102\5$\23\2\u0101\u00fe\3\2\2\2\u0102\u0105\3\2"+
		"\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104#\3\2\2\2\u0105\u0103"+
		"\3\2\2\2\u0106\u0107\b\23\1\2\u0107\u0108\5&\24\2\u0108\u010e\3\2\2\2"+
		"\u0109\u010a\f\4\2\2\u010a\u010b\7\6\2\2\u010b\u010d\5&\24\2\u010c\u0109"+
		"\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f"+
		"%\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\b\24\1\2\u0112\u0113\5(\25\2"+
		"\u0113\u0119\3\2\2\2\u0114\u0115\f\4\2\2\u0115\u0116\7\7\2\2\u0116\u0118"+
		"\5(\25\2\u0117\u0114\3\2\2\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119"+
		"\u011a\3\2\2\2\u011a\'\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\7\b\2\2"+
		"\u011d\u0120\5(\25\2\u011e\u0120\5*\26\2\u011f\u011c\3\2\2\2\u011f\u011e"+
		"\3\2\2\2\u0120)\3\2\2\2\u0121\u0122\7\t\2\2\u0122\u0125\5*\26\2\u0123"+
		"\u0125\5,\27\2\u0124\u0121\3\2\2\2\u0124\u0123\3\2\2\2\u0125+\3\2\2\2"+
		"\u0126\u0129\5.\30\2\u0127\u0129\5\60\31\2\u0128\u0126\3\2\2\2\u0128\u0127"+
		"\3\2\2\2\u0129-\3\2\2\2\u012a\u012f\5\60\31\2\u012b\u012c\7<\2\2\u012c"+
		"\u012d\5 \21\2\u012d\u012e\7=\2\2\u012e\u0130\3\2\2\2\u012f\u012b\3\2"+
		"\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132"+
		"/\3\2\2\2\u0133\u0136\5\66\34\2\u0134\u0136\5\62\32\2\u0135\u0133\3\2"+
		"\2\2\u0135\u0134\3\2\2\2\u0136\61\3\2\2\2\u0137\u013d\5\64\33\2\u0138"+
		"\u0139\7:\2\2\u0139\u013a\5 \21\2\u013a\u013b\7;\2\2\u013b\u013d\3\2\2"+
		"\2\u013c\u0137\3\2\2\2\u013c\u0138\3\2\2\2\u013d\63\3\2\2\2\u013e\u0142"+
		"\7\3\2\2\u013f\u0142\5<\37\2\u0140\u0142\5> \2\u0141\u013e\3\2\2\2\u0141"+
		"\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142\65\3\2\2\2\u0143\u0144\7\3\2"+
		"\2\u0144\u014f\7:\2\2\u0145\u014a\5 \21\2\u0146\u0147\7C\2\2\u0147\u0149"+
		"\5 \21\2\u0148\u0146\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a"+
		"\u014b\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u0145\3\2"+
		"\2\2\u014e\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150"+
		"\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0153\7;\2\2\u0153\67\3\2\2\2"+
		"\u0154\u0155\7<\2\2\u0155\u0156\5 \21\2\u0156\u0157\7=\2\2\u0157\u015e"+
		"\3\2\2\2\u0158\u0159\7<\2\2\u0159\u015a\5 \21\2\u015a\u015b\7=\2\2\u015b"+
		"\u015c\58\35\2\u015c\u015e\3\2\2\2\u015d\u0154\3\2\2\2\u015d\u0158\3\2"+
		"\2\2\u015e9\3\2\2\2\u015f\u0160\7\3\2\2\u0160\u0161\7D\2\2\u0161\u0162"+
		"\5> \2\u0162;\3\2\2\2\u0163\u0164\t\2\2\2\u0164=\3\2\2\2\u0165\u0174\7"+
		">\2\2\u0166\u0169\5<\37\2\u0167\u0169\5> \2\u0168\u0166\3\2\2\2\u0168"+
		"\u0167\3\2\2\2\u0169\u0171\3\2\2\2\u016a\u016d\7C\2\2\u016b\u016e\5<\37"+
		"\2\u016c\u016e\5> \2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e\u0170"+
		"\3\2\2\2\u016f\u016a\3\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171"+
		"\u0172\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0168\3\2"+
		"\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\7?\2\2\u0177"+
		"?\3\2\2\2\u0178\u017b\5D#\2\u0179\u017b\5B\"\2\u017a\u0178\3\2\2\2\u017a"+
		"\u0179\3\2\2\2\u017b\u0183\3\2\2\2\u017c\u017f\7C\2\2\u017d\u0180\5D#"+
		"\2\u017e\u0180\5B\"\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180\u0182"+
		"\3\2\2\2\u0181\u017c\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183"+
		"\u0184\3\2\2\2\u0184A\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u018a\7\3\2\2"+
		"\u0187\u0188\7<\2\2\u0188\u0189\7\n\2\2\u0189\u018b\7=\2\2\u018a\u0187"+
		"\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d"+
		"\u0190\3\2\2\2\u018e\u0190\7\3\2\2\u018f\u0186\3\2\2\2\u018f\u018e\3\2"+
		"\2\2\u0190\u0191\3\2\2\2\u0191\u0194\7D\2\2\u0192\u0195\5> \2\u0193\u0195"+
		"\5<\37\2\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195C\3\2\2\2\u0196"+
		"\u019a\7\3\2\2\u0197\u0198\7<\2\2\u0198\u0199\7\n\2\2\u0199\u019b\7=\2"+
		"\2\u019a\u0197\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d"+
		"\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u01a0\7\3\2\2\u019f\u0196\3\2\2\2\u019f"+
		"\u019e\3\2\2\2\u01a0E\3\2\2\2\u01a1\u01a6\7\3\2\2\u01a2\u01a3\7<\2\2\u01a3"+
		"\u01a4\5 \21\2\u01a4\u01a5\7=\2\2\u01a5\u01a7\3\2\2\2\u01a6\u01a2\3\2"+
		"\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9"+
		"G\3\2\2\2\u01aa\u01ab\5F$\2\u01ab\u01ac\7D\2\2\u01ac\u01ad\5> \2\u01ad"+
		"I\3\2\2\2\u01ae\u01af\7\3\2\2\u01af\u01b0\7D\2\2\u01b0\u01b1\5<\37\2\u01b1"+
		"K\3\2\2\2\u01b2\u01b7\5D#\2\u01b3\u01b4\7C\2\2\u01b4\u01b6\5D#\2\u01b5"+
		"\u01b3\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2"+
		"\2\2\u01b8M\3\2\2\2\u01b9\u01b7\3\2\2\2,SYhqw\u0082\u0088\u009e\u00ab"+
		"\u00b0\u00d6\u00e6\u00eb\u00f2\u00f9\u0103\u010e\u0119\u011f\u0124\u0128"+
		"\u0131\u0135\u013c\u0141\u014a\u014f\u015d\u0168\u016d\u0171\u0174\u017a"+
		"\u017f\u0183\u018c\u018f\u0194\u019c\u019f\u01a8\u01b7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}