import org.apache.bcel.classfile.ClassParser;
import org.apache.bcel.classfile.JavaClass;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;

/**
 * @author Arthur Kupriyanov
 */
public class Example {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = ClassParserExample.class.getResourceAsStream("./A.class");
        if (inputStream == null) throw new FileNotFoundException();

        ClassParser parser = new ClassParser(inputStream, "ClassA.class");

        JavaClass clazz = parser.parse();

        JasminVisitor jv = new JasminVisitor(clazz, System.out);

        jv.disassemble();

        clazz.accept(jv);
        clazz.getMethods()[1].accept(jv);

    }
}